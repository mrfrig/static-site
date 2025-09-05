import os
import shutil

static_path = "static"
public_path = "docs"


def copy_static_to_public(path=static_path):
    if (
        path == static_path
        and os.path.exists(public_path)
        and os.listdir(
            public_path,
        )
    ):
        shutil.rmtree(public_path)

    if not os.path.exists(public_path):
        os.mkdir(public_path)

    for name in os.listdir(path):
        filepath = path + "/" + name
        replacement = filepath.replace(f"{static_path}/", f"{public_path}/")
        if os.path.isfile(filepath):
            shutil.copy(filepath, replacement)
        else:
            os.mkdir(replacement)
            copy_static_to_public(filepath)
