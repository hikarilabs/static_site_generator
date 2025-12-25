class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by subclasses")

    def props_to_html(self):
        if self.props is None:
            return ""
        html_props = []
        for key, value in self.props.items():
            html_props.append(f' {key}="{value}"')
        return "".join(html_props)

    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={len(self.children)}, props={len(self.props)})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        if self.children is None:
            raise ValueError("ParentNode children cannot be None")
        html_children = []
        for child in self.children:
            html_children.append(child.to_html())
        return f'<{self.tag}{self.props_to_html()}>{"".join(html_children)}</{self.tag}>'

