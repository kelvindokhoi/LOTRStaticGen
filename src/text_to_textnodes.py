from textnode import TextNode,TextType
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter


def text_to_textnodes(text):
    if text=='':
        return []
    node = TextNode(text,TextType.TEXT,None)
    bolded = split_nodes_delimiter([node],'**',TextType.BOLD)
    italiced = split_nodes_delimiter(bolded,'_',TextType.ITALIC)
    coded = split_nodes_delimiter(italiced,'`',TextType.CODE)
    linked = split_nodes_link(coded)
    imaged = split_nodes_image(linked)
    return imaged