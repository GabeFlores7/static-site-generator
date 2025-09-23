import os
import shutil
from block_markdown import extract_title
from copystatic import copy_static_to
        
def main():
    src = "./static"
    dst = "./public"
    print("Deleting public directory...")
    # Delete everything in dst folder upon intial start of function
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Recursively copy static files to public directory 
    print("Copying static files to public directory...")
    copy_static_to(src, dst)

if __name__ == "__main__":
    main()