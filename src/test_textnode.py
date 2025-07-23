import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("Google",TextType.LINK,"google.com")
        node2 = TextNode("Google",TextType.LINK,"www.google.com")
        self.assertNotEqual(node,node2)
    
    def test_not_eq2(self):
        node = TextNode("Google",TextType.TEXT,"google.com")
        node2 = TextNode("Google",TextType.LINK,"google.com")
        self.assertNotEqual(node,node2)
    
    def test_not_eq3(self):
        node = TextNode("Googlez",TextType.LINK,"google.com")
        node2 = TextNode("Google",TextType.LINK,"google.com")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()