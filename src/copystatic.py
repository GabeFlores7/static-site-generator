import os
import shutil

def copy_static_to(src, dst):
    # If directory doesn't exist, make it
    if not os.path.exists(dst):
        os.mkdir(dst)
    # Begin copying all contents from 'src' to 'dst'
    src_contents = os.listdir(src)
    for src_item in src_contents:
        src_item_path = os.path.join(src, src_item)
        new_dst = os.path.join(dst, src_item)
        # Copy all files in directory
        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path, new_dst)
        # If new dst is not a file, recursively call function
        else:
            copy_static_to(src_item_path, new_dst)