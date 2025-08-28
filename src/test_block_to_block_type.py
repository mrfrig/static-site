import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_blocks(self):
        result = block_to_block_type("This is some paragraph")
        self.assertEqual(result, BlockType.PARAGRAPH)
        result = block_to_block_type(
            """This is some
multi line paragraph"""
        )
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading_blocks(self):
        result = block_to_block_type("# Heading 1")
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type("## Heading 2")
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type("### Heading 3")
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type("#### Heading 4")
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type("##### Heading 5")
        self.assertEqual(result, BlockType.HEADING)
        result = block_to_block_type("###### Heading 6")
        self.assertEqual(result, BlockType.HEADING)

    def test_not_heading_blocks(self):
        result = block_to_block_type("####### Heading 7?")
        self.assertNotEqual(result, BlockType.HEADING)
        result = block_to_block_type("#Heading?")
        self.assertNotEqual(result, BlockType.HEADING)

    def test_code_blocks(self):
        result = block_to_block_type("``````")
        self.assertEqual(result, BlockType.CODE)
        result = block_to_block_type("```This is a code block```")
        self.assertEqual(result, BlockType.CODE)

    def test_not_code_blocks(self):
        result = block_to_block_type("`This is not a code block`")
        self.assertNotEqual(result, BlockType.CODE)
        result = block_to_block_type("``This is not a code block``")
        self.assertNotEqual(result, BlockType.CODE)

    def test_quote_blocks(self):
        result = block_to_block_type(">")
        self.assertEqual(result, BlockType.QUOTE)
        result = block_to_block_type("> ")
        self.assertEqual(result, BlockType.QUOTE)
        result = block_to_block_type("> This is a quote block")
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list_blocks(self):
        result = block_to_block_type("- ")
        self.assertEqual(result, BlockType.UNORDERED_LIST)
        result = block_to_block_type("- This is an unordered list")
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list_blocks(self):
        result = block_to_block_type("-")
        self.assertNotEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list_blocks(self):
        result = block_to_block_type("1. Item 1")
        self.assertEqual(result, BlockType.ORDERED_LIST)
        result = block_to_block_type(
            """
            1. Item 1
2. Item 2
3. Item 3"""
        )
        self.assertEqual(result, BlockType.ORDERED_LIST)
        result = block_to_block_type(
            """1. Item 1
3. Item 3"""
        )
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_invalid_ordered_list_blocks(self):
        result = block_to_block_type("2. Item")
        self.assertNotEqual(result, BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
