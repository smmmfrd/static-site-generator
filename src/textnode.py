from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"


class TextNode:
    def __init__(self, text, text_type: TextType, url=""):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    tag = None
    value = text_node.text
    props = None

    if text_node.text_type is TextType.PLAIN_TEXT:
        tag = None
    elif text_node.text_type is TextType.BOLD_TEXT:
        tag = "b"
    elif text_node.text_type is TextType.ITALIC_TEXT:
        tag = "i"
    elif text_node.text_type is TextType.CODE_TEXT:
        tag = "code"
    elif text_node.text_type is TextType.LINK_TEXT:
        tag = "a"
        props = {"href": text_node.url, "target": "_blank"}
    elif text_node.text_type is TextType.IMAGE_TEXT:
        tag = "img"
        value = None
        props = {"src": text_node.url, "alt": text_node.text}

    return LeafNode(tag, value, props)
