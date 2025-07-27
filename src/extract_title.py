import re

def extract_title(markdown):
    pattern = r'\<h1\>([\d\D]*)\</h1\>'
    title = re.search(pattern,markdown)
    if not title:
        raise Exception("Title is not found.")
    return title.group(1)
