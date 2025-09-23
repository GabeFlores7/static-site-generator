import os
import shutil
from textnode import TextType, TextNode
def copy_src_to(src, dst, was_deleted = True):
    if not os.path.exists(src):
        raise Exception("invalid path: src")
    if not os.path.exists(dst):
        raise Exception("invalid path: dst")
    # Delete everything in dst folder upon intial start of function
    if not was_deleted:
        contents = os.listdir(dst)
        for item_name in contents:
            item_path = os.path.join(dst, item_name)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                else:
                    shutil.rmtree(item_path)
            except Exception as e:
                print(F"Unexpected error occurred: {e}")
    # Begin copying all contents from 'src' to 'dst'
    src_contents = os.listdir(src)
    for src_item in src_contents:
        src_item_path = os.path.join(src, src_item)
        # Copy all files in directory
        if os.path.isfile(src_item_path):
            dst_path = os.path.join(dst, src_item)
            shutil.copy(src_item_path, dst_path)
        # Check if directory to be copied exists in 'dst', does not copy pychache directory
        else:
            if src_item != "__pycache__":
                new_dst = os.path.join(dst, src_item)
                if not os.path.exists(new_dst):
                    os.mkdir(new_dst)
                copy_src_to(src_item_path, new_dst)
        
def main():
    src = "./static"
    dst = "./public"
    test_node = TextNode("This is some anchor text", TextType("link"), "https://www.boot.dev")
    print(test_node)
    copy_src_to(src, dst, False)

if __name__ == "__main__":
    main()