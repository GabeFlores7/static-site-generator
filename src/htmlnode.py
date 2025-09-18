# Class used to represent HTML nodes. It can be either block or inline. 
class HTMLNode:
    def __init__(self, tag= None, value= None, children= None, props= None):
        self.tag= tag
        self.value= value
        self.children= children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    # Method to convert props dict to string for HTML attributes representation
    def props_to_html(self):
        html_string = ""
        if self.props is not None:
            for prop in self.props:
                html_string += f" {prop}=\"{self.props[prop]}\""
        return html_string
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

# class to represent single HTML tag with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props= None):
        super().__init__(tag, value, None, props)
    # Method used to render leaf node as single HTML string. Uses inherited 'props_to_html' method
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"