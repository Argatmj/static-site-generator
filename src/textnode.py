from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "NORMAL"
    BOLD_TEXT = "BOLD"
    ITALIC_TEXT = "ITALIC"
    CODE_TEXT = "CODE"
    LINKS = "LINK"
    IMAGES = "IMAGES"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return self == value
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"