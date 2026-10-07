"""Fail closed when personal archives, demos, or broken site links reach a build."""

import html
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_PARTS = {".private", ".blog_saved", ".event", ".teaching", ".pregrado",
                 ".conference-paper", ".preprint"}
BLOCKED_ROUTE = re.compile(r"(?:^|/)(?:blog/first|blog/\.?pregrado|\.private)(?:/|$)")
# Distinctive markers from the removed personal posts; never print their content.
PERSONAL_MARKERS = ("chontaduro", "calarma", "el rocío", "my journey", "mi trayectoria")
SITE_HOST = "s-paez.github.io"
# A separate GitHub Pages project maintained outside this repository.
SIBLING_PROJECT = "/opticam_lc/"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.invalid_self_closing = []

    def handle_startendtag(self, tag, attrs):
        if tag in {"div", "section", "main", "article", "header", "footer",
                   "nav", "aside", "span", "p", "ul", "ol", "li"}:
            self.invalid_self_closing.append(tag)
        self.handle_starttag(tag, attrs)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = "href" if tag in {"a", "link"} else "src"
        if tag in {"a", "link", "img", "script", "iframe"} and attrs.get(key):
            self.urls.append(attrs[key])


def check(destination):
    errors = []
    if not (destination / "index.html").is_file():
        return ["Build destination has no index.html"]
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    for name in tracked:
        path = Path(name)
        # Deletions in the working tree are intentional before the next commit.
        if not name or not (ROOT / path).exists():
            continue
        if BLOCKED_PARTS.intersection(path.parts) or BLOCKED_ROUTE.search(name):
            errors.append(f"Excluded material is tracked by Git: {name}")
    for source in (ROOT / "content", ROOT / "static", ROOT / "assets"):
        for path in source.rglob("*"):
            name = path.relative_to(ROOT).as_posix()
            if BLOCKED_PARTS.intersection(path.parts) or BLOCKED_ROUTE.search(name):
                errors.append(f"Excluded material in a publishable source: {name}")
            if path.suffix == ".md" and re.search(
                    r"(?m)^private:\s*true\s*$", path.read_text()):
                errors.append(f"Move private content outside publishable sources: {name}")
    for path in destination.rglob("*"):
        name = path.relative_to(destination).as_posix()
        if BLOCKED_PARTS.intersection(path.parts) or BLOCKED_ROUTE.search(name):
            errors.append(f"Excluded route in artifact: {name}")
        if not path.is_file():
            continue
        if path.suffix in {".html", ".xml", ".json", ".txt", ".js"}:
            content = path.read_text(errors="replace")
            normalized = html.unescape(content).casefold()
            if any(marker in normalized for marker in PERSONAL_MARKERS):
                errors.append(f"Personal archive text found in artifact: {name}")
            if "/blog/first/" in normalized or "/blog/pregrado/" in normalized:
                errors.append(f"Personal archive reference found in artifact: {name}")
            if "googletagmanager.com" in normalized or "g-9cf41vfpqc" in normalized:
                errors.append(f"Removed analytics found in artifact: {name}")
        if path.suffix != ".html":
            continue
        parser = Links()
        parser.feed(content)
        if parser.invalid_self_closing:
            errors.append(f"Invalid self-closing HTML container in {name}: "
                          + ", ".join(sorted(set(parser.invalid_self_closing))))
        base = f"https://{SITE_HOST}/{name}"
        for url in parser.urls:
            parsed = urlparse(urljoin(base, url))
            if parsed.scheme not in {"http", "https"}:
                continue
            if parsed.netloc not in {SITE_HOST, "localhost:1313", "127.0.0.1:1313"}:
                continue
            if parsed.path.startswith(SIBLING_PROJECT):
                continue
            local = destination / unquote(parsed.path).lstrip("/")
            if not local.is_file() and not (local / "index.html").is_file():
                errors.append(f"Broken internal link in {name}: {parsed.path}")
    return sorted(set(errors))


if __name__ == "__main__":
    destination = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    errors = check(destination)
    if errors:
        print("Publication blocked:\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("Publication verified: no excluded archives or demos, no removed analytics, links valid.")
