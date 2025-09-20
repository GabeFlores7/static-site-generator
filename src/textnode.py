from enum import Enum
from htmlnode import LeafNode
# types of text nodes covered by the script
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
# Class used as an intermediate representation of inline text
class TextNode:
    def __init__(self, text, text_type, url= None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node2):
        return (
            self.text == node2.text,
            self.text_type == node2.text_type,
            self.url == node2.url,
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
# Function to convert text_node to a LeafNode of HTML_node class
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag= None, value= text_node.text, props= None)
        case TextType.BOLD:
            return LeafNode(tag= 'b', value= text_node.text, props= None)
        case TextType.ITALIC:
            return LeafNode(tag= 'i', value= text_node.text, props= None)
        case TextType.CODE:
            return LeafNode(tag= 'c', value= text_node.text, props= None)
        case TextType.LINK:
            return LeafNode(tag= 'a', value= text_node.text, props= {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag= 'img', value= '', props= {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("invalid text: 'text type'")