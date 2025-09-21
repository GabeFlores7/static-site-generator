import re
from textnode import TextNode, TextType
# Function to convert Markdown nodes to TextNodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        temp_list = []
        delimiter_count = 0
        sections = node.text.split(delimiter) # split node.text into sections by delimiter
        if len(sections) % 2 == 0: # Account for unmatching delimter
            raise Exception("inavlid Markdown: delimiter count") 
        for section in sections:
            if not section: # if section is empty
                delimiter_count += 1
                continue
            if delimiter_count % 2: # append TextNode where type depends on number of delimiter instances
                new_nodes.append(TextNode(section, text_type))
            else:
                new_nodes.append(TextNode(section, TextType.TEXT))
            delimiter_count += 1
    return new_nodes

# Function to convert Markdown Image nodes to TextNodes
def split_nodes_image(old_nodes):
    new_nodes= []
    for node in old_nodes:
        text = node.text
        if node.text_type != TextType.TEXT: # If node is not of type 'TEXT', append it and skip loop
            new_nodes.append(node)
            continue
        if not text: # if TextNode has no text, skip node
            continue
        matches = extract_markdown_images(node.text)
        if not matches: # if TextNode has no text matching markdown image pattern, append text as TextType.text
            new_nodes.append(node)
            continue
        for match in matches:
            sections = text.split(f"![{match[0]}]({match[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "": # If text did not start with a match, then append the normal text first
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

# Function to convert Markdown Link nodes to TextNodes
def split_nodes_link(old_nodes):
    new_nodes= []
    for node in old_nodes:
        text = node.text
        if node.text_type != TextType.TEXT: # If node is not of type 'TEXT', append it and skip loop
            new_nodes.append(node)
            continue
        if not text: # if TextNode has no text, skip node
            continue
        matches = extract_markdown_links(node.text)
        if not matches: # if TextNode has no text matching markdown image pattern, append text as TextType.text
            new_nodes.append(node)
            continue
        for match in matches:
            sections = text.split(f"[{match[0]}]({match[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "": # If text did not start with a match, then append the normal text first
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

# Function to extract links and images from Markdown using regex
def extract_markdown_images(text):
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(image_pattern, text)

def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(link_pattern, text)

#Function to convert Raw Markdown to TextNodes using 'split_nodes_fxn's'
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes