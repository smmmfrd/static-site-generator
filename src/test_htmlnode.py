import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode(value="Learn backend web development!")
        self.assertEqual(
            str(node),
            "HTMLNode (tag=None, value=Learn backend web development!, children=None, props=None)",
        )

    def test_props_link(self):
        t = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(
            t.props_to_html(), ' href="https://www.google.com" target="_blank" '
        )

    def test_props_image(self):
        t = HTMLNode(
            props={
                "src": "https://www.boot.dev/img/bootdev-logo-full-small.webp",
                "alt": "Boot.dev logo",
            }
        )
        self.assertEqual(
            t.props_to_html(),
            ' src="https://www.boot.dev/img/bootdev-logo-full-small.webp" alt="Boot.dev logo" ',
        )

    def test_leaf(self):
        t = LeafNode("p", "This is a paragraph of text.").to_html()

        self.assertEqual(t, "<p>This is a paragraph of text.</p>")

    def test_leaf_props(self):
        t = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com", "target": "_blank"}
        ).to_html()

        self.assertEqual(
            t, '<a href="https://www.google.com" target="_blank" >Click me!</a>'
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
