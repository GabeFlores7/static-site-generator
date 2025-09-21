
# Function converting raw Markdown string to list of 'block' strings
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_list = []
    for block in blocks:
        if block:
            block_list.append(block.strip())
    return block_list