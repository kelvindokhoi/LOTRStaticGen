from re import findall

def extract_markdown_links(text):
    pattern = r'(?<!\!)\[(.*?)\]\((.*?)\)'
    return findall(pattern,text)

if __name__=="__main__":
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))