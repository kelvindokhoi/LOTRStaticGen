import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )

    def test_empty_text(self):
        text = ""
        result = text_to_textnodes(text)
        self.assertListEqual([], result)

    def test_malformed_markdown(self):
        text = "This is **unclosed bold and [link](https://example.com)"
        with self.assertRaises(Exception) as context:
            text_to_textnodes(text)
        self.assertEqual(str(context.exception), "Incomplete pair of delimiter")

    def test_plain_text(self):
        text = "This is plain text with no formatting"
        result = text_to_textnodes(text)
        self.assertListEqual([TextNode("This is plain text with no formatting", TextType.TEXT)], result)

    def test_only_bold(self):
        text = "**bold text**"
        result = text_to_textnodes(text)
        self.assertListEqual([TextNode("bold text", TextType.BOLD)], result)

    def test_only_italic(self):
        text = "_italic text_"
        result = text_to_textnodes(text)
        self.assertListEqual([TextNode("italic text", TextType.ITALIC)], result)

    def test_only_code(self):
        text = "`code text`"
        result = text_to_textnodes(text)
        self.assertListEqual([TextNode("code text", TextType.CODE)], result)

    def test_only_image(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png)"
        result = text_to_textnodes(text)
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], result)

    def test_only_link(self):
        text = "[link](https://example.com)"
        result = text_to_textnodes(text)
        self.assertListEqual([TextNode("link", TextType.LINK, "https://example.com")], result)

    def test_mixed_formatting(self):
        text = "This is **bold** and _italic_ and `code`"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            result,
        )

    def test_consecutive_formatting(self):
        text = "**bold****another bold**_italic_`code`"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode("another bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code", TextType.CODE),
            ],
            result,
        )

    def test_image_and_link(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png)[link](https://example.com)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            result,
        )

    def test_nested_formatting(self):
        text = "This is **bold with _italic_ text**"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold with _italic_ text", TextType.BOLD),
            ],
            result,
        )

if __name__ == "__main__":
    unittest.main()