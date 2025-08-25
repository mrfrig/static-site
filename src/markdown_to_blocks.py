def markdown_to_blocks(markdown: str):
    split = markdown.split("\n\n")
    result = []
    for val in split:
        new_val = val.strip()
        if not new_val:
            continue
        result.append(new_val)
    return result
