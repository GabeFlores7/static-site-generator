import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
# 6 Tests for 'TextType' class
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("", TextType.CODE)
        node2 = TextNode("", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode(" A%$ ..", TextType.IMAGE, url= "https://www.boot.dev")
        node2 = TextNode(" A%$ ..", TextType.IMAGE, url= "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_false2(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.CODE)
        self.assertEqual(node, node2)

    def test_false3(self):
        node = TextNode("", TextType.CODE, url= "https://www.boot.dev")
        node2 = TextNode("", TextType.CODE, url= "https://www.boot.dev/")
        self.assertEqual(node, node2)
# 4 Tests for 'text_node_to_html_node' fxn
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )
    
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://open.spotify.com/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href":"https://open.spotify.com/"})

if __name__ == "__main__":
    unittest.main()