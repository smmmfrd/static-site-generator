class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if "href" in self.props:
            if "target" in self.props:
                return f' href="{self.props["href"]}" target="{self.props["target"]}" '
            else:
                return f' href="{self.props["href"]}" '

        elif "src" in self.props:
            return f' src="{self.props["src"]}" alt="{self.props["alt"]}" '
        return f"Not implemented"

    def __repr__(self):
        return f"HTMLNode (tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value.")

        if self.tag is None:
            return str(self.value)

        props = "" if self.props is None else self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")

        if self.children is None:
            raise ValueError("No children")

        html = f"<{self.tag}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html
