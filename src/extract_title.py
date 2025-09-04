def extract_title(markdown: str):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line.replace("# ", "", 1)
    raise Exception("No title found!")
