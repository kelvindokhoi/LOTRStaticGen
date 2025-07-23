from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old in old_nodes:
        if old.text_type == TextType.TEXT:
            temp_new = []
            trigger = False
            if old.text.count(delimiter)%2!=0:
                raise Exception("Incomplete pair of delimiter")
            for indiv_text in old.text.split(sep=delimiter):
                if indiv_text=="":
                    trigger = not trigger
                    continue
                if trigger:
                    temp_new.append(TextNode(indiv_text,text_type))
                else:
                    temp_new.append(TextNode(indiv_text,old.text_type))
                trigger = not trigger
            new_nodes.extend(temp_new)
        else:
            new_nodes.append(old)
    return new_nodes