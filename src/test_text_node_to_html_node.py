import unittest
from text_node_to_html_node import text_node_to_html_node
from htmlnode import HTMLNode,LeafNode
from textnode import TextNode,TextType

class Test_Text_Node_To_HTML_Node(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("Google",TextType.LINK,"google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'a')
        self.assertEqual(html_node.props,{'href':"google.com"})
    def test_bold(self):
        node = TextNode("BOLD text",TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,'b')
        self.assertEqual(html_node.value,"BOLD text")

if __name__=="__main__":
    unittest.main()