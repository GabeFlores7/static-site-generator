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
    
