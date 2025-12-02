import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is another text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_blank_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is some bold text.", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is some bold text.")

    def test_link_text(self):
        node = TextNode("This is a link!", TextType.LINK_TEXT, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link!")
        self.assertEqual(
            html_node.props, {"href": "https://www.google.com", "target": "_blank"}
        )

    def test_text(self):
        node = TextNode(
            "Boot.dev logo",
            TextType.IMAGE_TEXT,
            "https://www.boot.dev/img/bootdev-logo-full-small.webp",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {
                "src": "https://www.boot.dev/img/bootdev-logo-full-small.webp",
                "alt": "Boot.dev logo",
            },
        )


if __name__ == "__main__":
    unittest.main()
