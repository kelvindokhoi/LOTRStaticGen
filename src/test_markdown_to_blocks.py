import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "This is a single paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph"])

    def test_multiple_newlines(self):
        md = "First block\n\n\n\nSecond block\n\n\nThird block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block", "Third block"])

    def test_leading_trailing_whitespace(self):
        md = "\n\n  First block  \n\n\n  Second block  \n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_only_whitespace(self):
        md = "\n\n  \n\n\n  \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_mixed_block_types(self):
        md = """
# Heading

Paragraph with **bold** text

- List item 1
- List item 2

> Blockquote
> Second line
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "Paragraph with **bold** text",
                "- List item 1\n- List item 2",
                "> Blockquote\n> Second line",
            ],
        )

    def test_single_line_with_whitespace(self):
        md = "   Single line   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Single line"])

    def test_consecutive_newlines_within_block(self):
        md = """
Paragraph
with multiple
lines

Another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Paragraph\nwith multiple\nlines",
                "Another paragraph",
            ],
        )

if __name__ == "__main__":
    unittest.main()