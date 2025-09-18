import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
# 5 Tests for HTMLNode class
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_method_props_to_html(self):
        node= HTMLNode()
        node2= HTMLNode()
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_method_props_to_html3(self):
        props_input = {"href": "https://www.google.com", "target": "_blank"}

        node = HTMLNode(tag= "p",
        value= "This is a test",
        children= None,
        props= props_input)

        expected_html_string = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), expected_html_string)

    def test_false_method_props_to_html(self):
        props_input = {"href": "https://www.google.com", "target": "_blank"}
        props_input2 = {"href": "https://www.google.com.", "target": "_blank"}

        node = HTMLNode(tag= "p",
         value= "This is a test",
         children= None,
         props= props_input)

        node2 = HTMLNode(tag= "p",
        value= "This is a test",
        children= None,
        props= props_input2)
        
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
# 3 Tests for LeafNode class
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_result = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), expected_result)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")