from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
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


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        full_text = node.text
        matches = extract_markdown_images(full_text)
        if not matches:
            new_nodes.append(node)
            continue
        parts = re.split(r"(!\[.+?]\(.+?\))", full_text)
        for part in parts:
            if not part:
                continue
            match = extract_markdown_images(part)
            if match:
                new_nodes.append(TextNode(match[0][0], TextType.IMAGE, match[0][1]))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        full_text = node.text
        matches = extract_markdown_links(full_text)
        if not matches:
            new_nodes.append(node)
            continue
        parts = re.split(r"(\[.+?]\(.+?\))", full_text)
        for part in parts:
            if not part:
                continue
            match = extract_markdown_links(part)
            if match:
                new_nodes.append(TextNode(match[0][0], TextType.LINK, match[0][1]))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes
