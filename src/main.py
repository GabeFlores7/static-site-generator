import os
import shutil
from block_markdown import extract_title
from copystatic import copy_static_to
from page_generation import generate_page
        
def main():
    # 'copy_static_to' inputs
    static_path = "./static"
    public_path = "./public"
    # 'generate_pate' inputs
    content_path = "./content/index.md"
    template_path = "./template.html"
    webpage_path = "./public/index.html"

    print(f"Deleting {public_path.replace('./', '')} directory...")
    # Delete everything in dst folder upon intial start of function
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    # Recursively copy static files to public directory 
    print(f"Copying {static_path.replace('./', '')} files to {public_path.replace('./', '')} directory...")
    copy_static_to(static_path, public_path)
    # Generate page from 'content/index.md' uring 'template.html' and write to 'public/index.html'
    generate_page(content_path, template_path, webpage_path)

if __name__ == "__main__":
    main()