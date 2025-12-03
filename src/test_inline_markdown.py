import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)


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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )
