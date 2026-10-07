"""Regression checks for the publication gate, with synthetic public artifacts."""

import tempfile
import unittest
from pathlib import Path

from verify_publication import check


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

    def test_analytics_cannot_be_reintroduced(self):
        (self.site / "tracking.js").write_text("// G-9CF41VFPQC")
        self.assertTrue(any("analytics" in e for e in check(self.site)))

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
