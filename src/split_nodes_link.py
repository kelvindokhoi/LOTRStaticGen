from textnode import TextNode,TextType
from extract_markdown_links import extract_markdown_links
from re import finditer


def split_nodes_link(old_nodes):
    pattern = r'(?<!\!)\[(.*?)\]\((.*?)\)'
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            new_node = []
            matches = [(match.start(),match.end()) for match in finditer(pattern,old_node.text)]
            if not matches:
                new_nodes.append(old_node)
                continue
            last_seen = 0
            for start,end in matches:
                if start==last_seen:
                    result = extract_markdown_links(old_node.text[start:end])[0]
                    new_node.append(TextNode(result[0],TextType.LINK,result[1]))
                else:
                    if old_node.text[last_seen:start]:
                        new_node.append(TextNode(old_node.text[last_seen:start],TextType.TEXT,))
                    result = extract_markdown_links(old_node.text[start:end])[0]
                    new_node.append(TextNode(result[0],TextType.LINK,result[1]))
                last_seen = end
            if last_seen<len(old_node.text):
                if old_node.text[last_seen:]:
                    new_node.append(TextNode(old_node.text[last_seen:],TextType.TEXT,))
            new_nodes.extend(new_node)
        else:
            new_nodes.append(old_node)
    return new_nodes