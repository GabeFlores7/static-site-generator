import os
from markdown_to_html import markdown_to_html_node
from block_markdown import extract_title

# Function to generate and serve webpage
def generate_page(from_path, template_path, dest_path):
    # Function initialization/ read files
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, mode= 'r') as f:
        md_file = f.read()
    with open(template_path, mode= 'r') as f:
        template_file = f.read()

    # Convert Markdown to string and extract title
    html_content = markdown_to_html_node(md_file).to_html()
    html_title = extract_title(md_file)
    # Modify template content
    webpage = template_file.replace("{{ Content }}", html_content)
    webpage = webpage.replace("{{ Title }}", html_title)

    # Make 'destination directory' if non-existent
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # Write file to 'dest_path'
    with open(dest_path, mode= 'w') as f:
        f.write(webpage)
    