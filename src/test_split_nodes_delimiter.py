import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode,TextType

class Test_Split_Nodes_Delimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],'**',TextType.BOLD)
        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ])
    
    def test_itallic(self):
        node = TextNode("This is text with a _itallic_ word",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],'_',TextType.ITALIC)
        self.assertEqual(new_nodes,[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("itallic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

if __name__ == "__main__":
    unittest.main()