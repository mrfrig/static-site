from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid Markdown syntax")

        full_text = node.text
        parts = full_text.split(delimiter)

        for part in parts:
            if not part:
                continue
            to_replace = part
            if f"{delimiter}{part}{delimiter}" in full_text:
                new_nodes.append(TextNode(part, text_type))
                to_replace = f"{delimiter}{part}{delimiter}"
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
            full_text = full_text.replace(to_replace, "")
    return new_nodes
