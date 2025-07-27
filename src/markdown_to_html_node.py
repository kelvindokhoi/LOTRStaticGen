from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,TextType
from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_blocktype
from blocktype import BlockType
import re
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    div_html_node = ParentNode('div',None,None)
    for markdown_block in markdown_blocks:
        block_type = block_to_blocktype(markdown_block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = ParentNode('p',None,None)
            case BlockType.HEADING:
                html_node = ParentNode(heading_block_to_html_tag(markdown_block),None,{})
            case BlockType.CODE:
                html_node = ParentNode('pre',None,None)
            case BlockType.QUOTE:
                html_node = ParentNode('blockquote',None,None)
            case BlockType.UNORDERED_LIST:
                html_node = ParentNode('ul',None,None)
            case BlockType.ORDERED_LIST:
                html_node = ParentNode('ol',None,None)
        match html_node.tag:
            case 'pre':
                html_node.children = [text_node_to_html_node(TextNode('\n'.join([markdown_line.lstrip(' ').rstrip(' ') for markdown_line in markdown_block.split('\n')][1:-1])+'\n',TextType.CODE,None))]
            case 'blockquote':
                processed_markdown_block = '\n'.join(markdown_line[2:]for markdown_line in markdown_block.split('\n'))
                html_node.children = text_to_children(processed_markdown_block)
            case 'ul','ol':
                processed_markdown_block = [markdown_line[re.match(r'^(\-|\*|\d+\.) ',markdown_line).end():] for markdown_line in markdown_block.split('\n')] # type: ignore
                html_node.children = [ParentNode('li',None,text_to_children(processed_markdown_line)) for processed_markdown_line in processed_markdown_block]
            case 'p':
                processed_markdown_block = '\n'.join(' '.join(markdown_line.lstrip(' ').rstrip(' ') for markdown_line in filter(lambda markdown_line:markdown_line.strip()!='',markdown_paragraph.split('\n'))) for markdown_paragraph in markdown_block.split('\n\n'))
                html_node.children = text_to_children(processed_markdown_block)
            case _:
                html_node.children = text_to_children(markdown_block)
            
        if div_html_node.children is None:
            div_html_node.children = [html_node]
        else:
            div_html_node.children.append(html_node)
    return div_html_node

def heading_block_to_html_tag(markdown):
    power = re.search(r'^(#{1,6})',markdown)
    if power is None:
        raise Exception('No # indicator detected!')
    return 'h'+str(len(power.group(1)))

def text_to_children(markdown):
    lines = markdown.split(sep='\n')
    children = []
    for line in lines:
        line_html_nodes = [text_node_to_html_node(node) for node in text_to_textnodes(line)]
        children.extend(line_html_nodes)
    return children
