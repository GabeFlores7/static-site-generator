import os
from markdown_to_html import markdown_to_html_node
from block_markdown import extract_title

# Function to generate and serve webpage
def generate_page(from_path, template_path, dest_path, basepath):
    # Function initialization read files
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
    webpage = webpage.replace("href=\"/", f"href=\"{basepath}")
    webpage = webpage.replace("src=\"/", f"src=\"{basepath}")

    # Make 'destination directory' if non-existent
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # Write file to 'dest_path'
    with open(dest_path, mode= 'w') as f:
        f.write(webpage)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # Make dest path if nonexistent
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    # Store content entries into a list using input 'dir_path_content'
    entries_list = os.listdir(dir_path_content)
    # Make webpage if entry is file. Recurively call function if directory
    for entry in entries_list:
        content_entry_path = os.path.join(dir_path_content, entry)
        new_dst_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(content_entry_path):
            new_dst_path = new_dst_path.replace('.md', '.html') # correct file extension
            generate_page(content_entry_path, template_path, new_dst_path, basepath)
        else:
            generate_pages_recursive(content_entry_path, template_path, new_dst_path, basepath)