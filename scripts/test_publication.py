"""Regression checks for the publication gate, with synthetic public artifacts."""

import tempfile
import unittest
from pathlib import Path

from verify_publication import GOOGLE_ANALYTICS_ID, check


SITE_HEAD = '<meta name="generator" content="Hugo Blox Builder 0.3.1">'
ANALYTICS_LOADER = (
    '<script async src="https://www.googletagmanager.com/gtag/js?id='
    + GOOGLE_ANALYTICS_ID + '"></script>')
ANALYTICS_CONFIG = (
    "<script>window.dataLayer = window.dataLayer || [];"
    "function gtag(){dataLayer.push(arguments);}"
    "gtag('js', new Date());"
    "gtag('config', '" + GOOGLE_ANALYTICS_ID + "', {});</script>")


class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.site = Path(self.temp.name)
        (self.site / "index.html").write_text('<a href="/about/">About</a>')
        (self.site / "about").mkdir()
        (self.site / "about/index.html").write_text("Public biography")

    def test_public_site_passes(self):
        self.assertEqual(check(self.site), [])

    def test_broken_internal_link_blocks_publication(self):
        (self.site / "index.html").write_text('<a href="/missing/">Missing</a>')
        self.assertTrue(any("Broken internal link" in e for e in check(self.site)))

    def test_personal_text_in_feed_blocks_publication(self):
        (self.site / "index.xml").write_text("<title>My journey</title>")
        self.assertTrue(any("Personal archive text" in e for e in check(self.site)))

    def test_personal_route_with_innocuous_text_is_blocked(self):
        private = self.site / "blog/first/index.html"
        private.parent.mkdir(parents=True)
        private.write_text("A generic title")
        self.assertTrue(any("Excluded route" in e for e in check(self.site)))

    def test_site_with_analytics_passes(self):
        (self.site / "index.html").write_text(
            SITE_HEAD + ANALYTICS_LOADER + ANALYTICS_CONFIG)
        self.assertEqual(check(self.site), [])

    def test_missing_analytics_blocks_publication(self):
        (self.site / "index.html").write_text(SITE_HEAD)
        self.assertTrue(any("Google Analytics" in e for e in check(self.site)))

    def test_analytics_loader_without_initialization_blocks_publication(self):
        (self.site / "index.html").write_text(SITE_HEAD + ANALYTICS_LOADER)
        self.assertTrue(any("Google Analytics config" in e for e in check(self.site)))

    def test_analytics_initialization_without_loader_blocks_publication(self):
        (self.site / "index.html").write_text(SITE_HEAD + ANALYTICS_CONFIG)
        self.assertTrue(any("Google Analytics loader" in e for e in check(self.site)))

    def test_wrong_measurement_id_blocks_publication(self):
        page = SITE_HEAD + ANALYTICS_LOADER + ANALYTICS_CONFIG
        (self.site / "index.html").write_text(
            page.replace(GOOGLE_ANALYTICS_ID, "G-WRONG12345"))
        self.assertTrue(any("Google Analytics" in e for e in check(self.site)))

    def test_duplicate_analytics_blocks_publication(self):
        (self.site / "index.html").write_text(
            SITE_HEAD + (ANALYTICS_LOADER + ANALYTICS_CONFIG) * 2)
        self.assertTrue(any("Google Analytics" in e for e in check(self.site)))

    def test_missing_analytics_in_spanish_blocks_publication(self):
        (self.site / "index.html").write_text(
            SITE_HEAD + ANALYTICS_LOADER + ANALYTICS_CONFIG)
        (self.site / "es").mkdir()
        (self.site / "es/index.html").write_text(SITE_HEAD)
        self.assertTrue(any("Google Analytics" in e and "es/index.html" in e
                            for e in check(self.site)))

    def test_self_closing_container_blocks_publication(self):
        (self.site / "index.html").write_text(
            '<section><div class="home-section-bg"/><div>Skills</div></section>')
        self.assertTrue(any("Invalid self-closing HTML" in e for e in check(self.site)))

    def test_valid_empty_container_passes(self):
        (self.site / "index.html").write_text(
            '<section><div class="home-section-bg"></div><div>Skills</div></section>')
        self.assertEqual(check(self.site), [])


if __name__ == "__main__":
    unittest.main()
