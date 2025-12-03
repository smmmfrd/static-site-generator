from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node(node, delimiter, text_type))

    return new_nodes


def split_node(old_node: TextNode, delimiter, text_type):
    if old_node.text_type != TextType.PLAIN_TEXT:
        return [old_node]

    divided = old_node.text.split(delimiter)

    if len(divided) % 2 != 1:
        raise Exception("Unenclosed markdown detected")

    new_nodes = [TextNode(divided[0], TextType.PLAIN_TEXT)]
    for i in range(1, len(divided)):
        type = text_type if i % 2 == 1 else TextType.PLAIN_TEXT

        new_nodes.append(TextNode(divided[i], type))

    return new_nodes
