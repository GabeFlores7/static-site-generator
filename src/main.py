import sys
import os
import shutil
from block_markdown import extract_title
from copystatic import copy_static_to
from page_generation import generate_pages_recursive
        
def main():
    # Configure root
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    # 'copy_static_to' inputs
    static_path = "./static"
    webpage_path = "./docs"
    # 'generate_pate' inputs
    content_path = "./content"
    template_path = "./template.html"

    print(f"Deleting {webpage_path.replace('./', '')} directory...")
    # Delete everything in dst folder upon intial start of function
    if os.path.exists(webpage_path):
        shutil.rmtree(webpage_path)
    # Recursively copy static files to docs directory 
    print(f"Copying {static_path.replace('./', '')} files to {webpage_path.replace('./', '')} directory...")
    copy_static_to(static_path, webpage_path)
    # Generate pages from 'content' using 'template.html' and write to 'docs'
    generate_pages_recursive(content_path, template_path, webpage_path, basepath)

if __name__ == "__main__":
    main()