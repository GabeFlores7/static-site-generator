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