from enum import Enum
# types of BlockTypes covered by the script
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

# Function converting raw Markdown string to list of 'block' strings
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_list = []
    for block in blocks:
        if block:
            block_list.append(block.strip())
    return block_list

# Function that takes block of markdown and returns corresponding BlockType
def block_to_block_type(block):
    if block.startswith(('#', '##', '###', '####', '#####', '######')):
        return BlockType.HEADING
    lines = block.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"): # Check for QUOTE
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "): # Check for Unordered List
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "): # check for Ordered List
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

# Function that takes Markdown input and returns the h1 header
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith('# '):
            return block.replace('# ', '').strip()
    raise Exception("Invalid Markdown: No h1 header")
    