from inline_markdown import text_to_textnodes
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import ParentNode

# Function to convert Markdown doc into single parent HTMLNode
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in markdown_blocks:
        match block_to_block_type(block):
            # Create HTMLNode with children that corresponds with any 6 of the BlockTypes
            case BlockType.PARAGRAPH:
                html_node = paragraph_block_to_html_node(block)
                block_nodes.append(html_node)

            case BlockType.HEADING:
                html_node = heading_block_to_html_node(block)
                block_nodes.append(html_node)

            case BlockType.CODE:
                html_node = code_block_to_html_node(block)
                block_nodes.append(html_node)

            case BlockType.QUOTE:
                html_node = quote_block_to_html_node(block)
                block_nodes.append(html_node)

            case BlockType.ULIST:
                html_node = ulist_block_to_html_node(block)
                block_nodes.append(html_node)

            case BlockType.OLIST:
                html_node = olist_block_to_html_node(block)
                block_nodes.append(html_node)

    return ParentNode(tag= "div", children= block_nodes)
# 7 Helper functions used in 'markdown_to_html_node'
def paragraph_block_to_html_node(markdown_block):
    inline_text = " ".join(markdown_block.split("\n")).strip() # clean up block for processing
    children_nodes = text_to_children(inline_text)
    return ParentNode('p', children_nodes)

def heading_block_to_html_node(markdown_block):
    text = markdown_block.strip()
    head_num = 0
    while text[head_num] == '#':
        head_num += 1
    children_nodes = text_to_children(text[head_num+1:])
    return ParentNode(f"h{head_num}", children_nodes)

def code_block_to_html_node(markdown_block):
    text = markdown_block.replace('`','').lstrip()
    code_node = TextNode(text, TextType.CODE)
    html_node = text_node_to_html_node(code_node)
    return ParentNode('pre', [html_node])

def quote_block_to_html_node(markdown_block):
    lines = markdown_block.strip().split("\n")
    clean_lines = []
    for line in lines:
        if line:
            clean_lines.append(line[2:]) # exclude '> ' in each line
    text = " ".join(clean_lines)
    children_nodes = text_to_children(text)
    return ParentNode('blockquote', children_nodes)

def ulist_block_to_html_node(markdown_block):
    lines = markdown_block.strip().split("\n")
    list_nodes = []
    for line in lines:
        item_children = text_to_children(line[2:]) # exclude '- ' in each line
        list_item = ParentNode('li', item_children)
        list_nodes.append(list_item)
    return ParentNode('ul', list_nodes)

def olist_block_to_html_node(markdown_block):
    lines = markdown_block.strip().split("\n")
    list_nodes = []
    for i in range(0, len(lines)):
        text = lines[i].replace(f"{i+1}. ", "") # exclude 'n. ' in each line
        item_children = text_to_children(text)
        list_item = ParentNode('li', item_children)
        list_nodes.append(list_item)
    return ParentNode('ol', list_nodes)

# Converts markdown to html nodes
def text_to_children(text):
    html_nodes = []
    nodes = text_to_textnodes(text) # convert markdown to text_nodes
    for node in nodes:# convert text_nodes to html_nodes
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
