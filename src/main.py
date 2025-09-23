import os
import shutil
from block_markdown import extract_title
from copystatic import copy_static_to
from page_generation import generate_pages_recursive
        
def main():
    # 'copy_static_to' inputs
    static_path = "./static"
    public_path = "./public"
    # 'generate_pate' inputs
    content_path = "./content"
    template_path = "./template.html"

    print(f"Deleting {public_path.replace('./', '')} directory...")
    # Delete everything in dst folder upon intial start of function
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    # Recursively copy static files to public directory 
    print(f"Copying {static_path.replace('./', '')} files to {public_path.replace('./', '')} directory...")
    copy_static_to(static_path, public_path)
    # Generate pages from 'content' using 'template.html' and write to 'public'
    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == "__main__":
    main()