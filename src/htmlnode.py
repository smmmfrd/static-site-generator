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
            return f' href="{self.props["href"]}" target="{self.props["target"]}" '

        elif "src" in self.props:
            return f' img src="{self.props["src"]}" alt="{self.props["alt"]}" '
        return f"Not implemented"

    def __repr__(self):
        return f"HTMLNode (tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
