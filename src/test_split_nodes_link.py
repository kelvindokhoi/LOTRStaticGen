import unittest
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class Test_Split_Nodes_Link(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://test.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://test.com"),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode("This is plain text without links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_only_link(self):
        node = TextNode("[link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("link", TextType.LINK, "https://example.com")],
            new_nodes,
        )

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_link_at_start(self):
        node = TextNode(
            "[link](https://example.com) followed by text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" followed by text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_at_end(self):
        node = TextNode(
            "Text before [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_multiple_nodes(self):
        nodes = [
            TextNode("Text with [link](https://example.com)", TextType.TEXT),
            TextNode("Plain text", TextType.TEXT),
            TextNode("[another](https://test.com)", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode("Plain text", TextType.TEXT),
                TextNode("another", TextType.LINK, "https://test.com"),
            ],
            new_nodes,
        )

    def test_non_text_node(self):
        node = TextNode("Some bold text", TextType.BOLD)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_consecutive_links(self):
        node = TextNode(
            "[link1](https://example.com)[link2](https://test.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link1", TextType.LINK, "https://example.com"),
                TextNode("link2", TextType.LINK, "https://test.com"),
            ],
            new_nodes,
        )

    def test_mixed_node_types(self):
        nodes = [
            TextNode("Text with [link](https://example.com)", TextType.TEXT),
            TextNode("Italic text", TextType.ITALIC),
            TextNode("[another](https://test.com)", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode("Italic text", TextType.ITALIC),
                TextNode("another", TextType.LINK, "https://test.com"),
            ],
            new_nodes,
        )

    def test_image_and_link(self):
        node = TextNode(
            "Text with ![image](https://i.imgur.com/zjjcJKZ.png) and [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text with ![image](https://i.imgur.com/zjjcJKZ.png) and ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()