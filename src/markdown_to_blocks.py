


def markdown_to_blocks(markdown):
    blocks = markdown.split(sep="\n\n")
    stripped_blocks = []
    for block in blocks:
        block = block.strip()
        if block:
            stripped_blocks.append(block)
    return stripped_blocks