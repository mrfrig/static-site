import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_input(self):
        text = "This is just text"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [TextNode("This is just text", TextType.TEXT)],
        )

    def test_bold_text_input(self):
        text = "**This is BOLD text**"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [
                TextNode("This is BOLD text", TextType.BOLD),
            ],
        )

    def test_italic_text_input(self):
        text = "_This is ITALIC text_"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [
                TextNode("This is ITALIC text", TextType.ITALIC),
            ],
        )

    def test_code_block_text_input(self):
        text = "`This is CODE text`"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [
                TextNode("This is CODE text", TextType.CODE),
            ],
        )

    def test_image_text_input(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
            ],
        )

    def test_link_text_input(self):
        text = "[link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_mixed_input_to_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
