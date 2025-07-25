from re import findall


def extract_markdown_images(text):
    pattern = r'\!\[(.*?)\]\((.*?)\)'
    return findall(pattern,text)


if __name__=="__main__":
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))