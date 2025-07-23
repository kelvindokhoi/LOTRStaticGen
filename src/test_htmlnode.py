import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_init_eq(self):
        htmlnode = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        htmlnode2 = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        self.assertEqual(htmlnode,htmlnode2)
    
    def test_init_neq(self):
        htmlnode = HTMLNode("p","simple value",[],{"href": "https://www.google.com"})
        htmlnode2 = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        self.assertFalse(htmlnode==htmlnode2)
    
    def test_init_neq2(self):
        htmlnode = HTMLNode("a","simple value",[],{"href": "https://www.googlez.com"})
        htmlnode2 = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        self.assertFalse(htmlnode==htmlnode2)

    def test_init_neq3(self):
        htmlnode = HTMLNode("a","simple valuesssss",[],{"href": "https://www.google.com"})
        htmlnode2 = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        self.assertNotEqual(htmlnode,htmlnode2)
    
    def test_init_neq4(self):
        child = HTMLNode("a","another simple value",[],{"href": "https://www.google.com"})
        htmlnode = HTMLNode("a","simple value",[child],{"href": "https://www.google.com"})
        htmlnode2 = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        self.assertNotEqual(htmlnode,htmlnode2)
    
    def test_props_to_html(self):
        htmlnode = HTMLNode("a","simple value",[],{"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(htmlnode.props_to_html(), expected)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click me!</a>')

    def test_leaf_to_html_tag_none(self):
        node = LeafNode(None, "Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")

    def test_leaf_to_html_value_none_raises(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_props_multiple(self):
        node = LeafNode("img", "alt text", {"src": "file.png", "width": "100"})
        result = node.to_html()
        self.assertTrue(result.startswith('<img'))
        self.assertIn('src="file.png"', result)
        self.assertIn('width="100"', result)
        self.assertTrue(result.endswith('>alt text</img>'))

class TestParentNode(unittest.TestCase):
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
    
    def test_to_html_with_multiple_leafnodes(self):
        childnode1 = LeafNode("span", "child")
        childnode2 = LeafNode("a", "Click me!", {"href": "https://www.example.com"})
        childnode3 = LeafNode("img", "alt text", {"src": "file.png", "width": "100"})
        parent_node = ParentNode("html",[childnode1,childnode2,childnode3])
        self.assertEqual(
            parent_node.to_html(),
            "<html><span>child</span><a href=\"https://www.example.com\">Click me!</a><img src=\"file.png\" width=\"100\">alt text</img></html>",
        )

if __name__ == "__main__":
    unittest.main()