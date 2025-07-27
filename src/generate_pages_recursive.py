import os
from generate_page import generate_page

def generate_pages_recursive(basepath,dir_path_content, template_path, dest_dir_path):
    if os.path.isdir(dir_path_content):
        os.makedirs(dest_dir_path,exist_ok=True)
        for item in os.listdir(dir_path_content):
            generate_pages_recursive(basepath,os.path.join(dir_path_content,item),template_path,os.path.join(dest_dir_path,item))
    else:
        generate_page(basepath,dir_path_content,template_path,dest_dir_path.replace('.md','.html'))
        
    
