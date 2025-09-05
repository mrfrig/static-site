import sys

from copy_static_to_public import public_path, copy_static_to_public
from generate_page import generate_pages_recursive


def main():
    try:
        basepath = sys.argv[1]
    except IndexError:
        basepath = "/"

    copy_static_to_public()
    print("basepath: ", basepath)
    generate_pages_recursive(
        "content",
        "./template.html",
        public_path,
        basepath,
    )


if __name__ == "__main__":
    main()
