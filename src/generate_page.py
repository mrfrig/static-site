import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    page = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", content)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(
    dir_path_content,
    template_path,
    dest_dir_path,
    basepath,
):
    for name in os.listdir(dir_path_content):
        file_path = dir_path_content + "/" + name
        dest_path = dest_dir_path + "/" + name
        if os.path.isfile(file_path):
            if name.endswith(".md"):
                generate_page(
                    file_path,
                    template_path,
                    dest_path.replace(".md", ".html"),
                    basepath,
                )
        else:
            generate_pages_recursive(
                file_path,
                template_path,
                dest_path,
                basepath,
            )
