import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()