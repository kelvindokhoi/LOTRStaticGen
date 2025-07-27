import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_path,template_path,dest_path = os.path.abspath(from_path),os.path.abspath(template_path),os.path.abspath(dest_path)

    with open(from_path, 'r') as f:
        markdown_file = f.read()

    with open(template_path, 'r') as f:
        template_file = f.read()

    html_string = markdown_to_html_node(markdown_file).to_html()
    html_title = extract_title(html_string)
    template_file = template_file.replace(r'{{ Title }}',html_title).replace(r'{{ Content }}',html_string)
    
    # os.makedirs(dest_path,exist_ok=True)
    with open(dest_path,'w'if os.path.exists(dest_path)else'x') as f:
        f.write(template_file)
