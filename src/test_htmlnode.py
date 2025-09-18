import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

# 3 Tests for ParentNode class
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        test_props = {"href": "https://www.google.com","target": "_blank"}
        great_grandchild_node = LeafNode("li", "Item 1", test_props)
        great_grandchild_node2 = LeafNode("li", "Item 2")
        great_grandchild_node3 = LeafNode("li", "Item 3")
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("i", "grandchild 2!")
        grandchild_node3 = ParentNode("ol", [great_grandchild_node, great_grandchild_node2, great_grandchild_node3])
        child_node = ParentNode("span", [grandchild_node, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><i>grandchild 2!</i><ol><li href=\"https://www.google.com\" target=\"_blank\">Item 1</li><li>Item 2</li><li>Item 3</li></ol></span></div>",
        )
