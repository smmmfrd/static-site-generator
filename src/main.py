import os
import shutil

from block_markdown import markdown_to_html_node, extract_title

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_templates = "./"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public dir...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page from content/...")
    content_path = os.path.join(dir_path_content, "index.md")
    template_path = os.path.join(dir_path_templates, "template.html")
    html_path = os.path.join(dir_path_public, "index.html")
    generate_page(content_path, template_path, html_path)


def copy_files_recursive(source_path, target_path):
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        dest_path = os.path.join(target_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md = md_file.read()
        with open(template_path) as template_file:
            template = template_file.read()

            title = extract_title(md)
            html = markdown_to_html_node(md).to_html()

            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)

            dest_dir_path = os.path.dirname(dest_path)
            if dest_dir_path != "":
                os.makedirs(dest_dir_path, exist_ok=True)

            to_file = open(dest_path, "w")
            to_file.write(template)


main()
