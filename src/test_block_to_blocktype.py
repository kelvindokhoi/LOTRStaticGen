import unittest
from block_to_blocktype import block_to_blocktype
from blocktype import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_single_level(self):
        block = "# Heading"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_multi_level(self):
        block = "#### Heading Level 4"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_code_block(self):
        block = "```\ncode here\nmore code\n```"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote_block(self):
        block = "> Quote line 1\n> Quote line 2"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is a normal paragraph\nwith multiple lines"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_empty_block(self):
        block = ""
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_single_line_paragraph(self):
        block = "Just a single line"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading_invalid_no_space(self):
        block = "#NoSpaceHeading"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading_too_many_hashes(self):
        block = "####### Seven hashes"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_block_incomplete(self):
        block = "```\ncode here\n"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_quote_block_partial(self):
        block = "> Quote line\nNot a quote"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_unordered_list_partial(self):
        block = "- Item 1\nNot a list item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_non_sequential(self):
        block = "1. First item\n3. Third item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_wrong_format(self):
        block = "1) First item\n2) Second item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_mixed_content(self):
        block = "# Heading\nNot a heading"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_single_line_quote(self):
        block = "> Single quote"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_single_line_unordered_list(self):
        block = "- Single item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_single_line_ordered_list(self):
        block = "1. Single item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ordered_list_starts_not_at_one(self):
        block = "2. Second item\n3. Third item"
        result = block_to_blocktype(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()