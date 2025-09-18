# Code used as an intermediate representation of inline text
from enum import Enum
# types of text nodes covered by the script
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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