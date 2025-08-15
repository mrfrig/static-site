import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "some link",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_empty_props_to_html(self):
        node = HTMLNode(
            "a",
            "some link",
            props={},
        )
        self.assertEqual(node.props_to_html(), "")

    def test_no_props_to_html(self):
        node = HTMLNode("a", "some link")
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
