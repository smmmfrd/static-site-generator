import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
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

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN_TEXT),
                TextNode("to boot dev", TextType.LINK_TEXT, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode(
                    "to youtube",
                    TextType.LINK_TEXT,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_split_no_link(self):
        node = TextNode(
            "This is text with no link",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is text with no link",
                    TextType.PLAIN_TEXT,
                )
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode(
                    "image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE_TEXT,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_split_text(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE_TEXT,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
            ],
            new_nodes,
        )
