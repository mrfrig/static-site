from copy_static_to_public import copy_static_to_public
from generate_page import generate_page


def main():
    copy_static_to_public()
    generate_page("content/index.md", "./template.html", "public/index.html")
    generate_page(
        "content/contact/index.md",
        "./template.html",
        "public/contact/index.html",
    )
    generate_page(
        "content/blog/glorfindel/index.md",
        "./template.html",
        "public/blog/glorfindel/index.html",
    )
    generate_page(
        "content/blog/majesty/index.md",
        "./template.html",
        "public/blog/majesty/index.html",
    )
    generate_page(
        "content/blog/tom/index.md",
        "./template.html",
        "public/blog/tom/index.html",
    )


if __name__ == "__main__":
    main()
