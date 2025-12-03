import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_bold(self):
        node = TextNode(
            "Learn **backend** web development!",
            TextType.PLAIN_TEXT,
        )
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("Learn ", TextType.PLAIN_TEXT),
                TextNode("backend", TextType.BOLD_TEXT),
                TextNode(" web development!", TextType.PLAIN_TEXT),
            ],
        )

    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" word", TextType.PLAIN_TEXT),
            ],
        )
