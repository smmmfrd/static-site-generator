import unittest

from block_markdown import BlockType, markdown_to_blocks, block_to_block_type


class TestBlockMarkdown(unittest.TestCase):
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

    def test_block_heading(self):
        block_type = block_to_block_type("# Dumb Heading")
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_code(self):
        block_type = block_to_block_type("``` Some dumb code.```")
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_quote(self):
        block_type = block_to_block_type("> Dumb Quote")
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_u_list(self):
        block_type = block_to_block_type("- Dumb List")
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_o_list(self):
        block_type = block_to_block_type(
            """1. First Dumb.
2. Second Dumb"""
        )
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
