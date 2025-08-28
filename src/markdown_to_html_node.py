from block_to_block_type import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown: str):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        if type == BlockType.PARAGRAPH:
            block = " ".join(block.split())
            text_nodes = text_to_textnodes(block)
            html_nodes = list(map(text_node_to_html_node, text_nodes))
            children.append(ParentNode("p", html_nodes))
        elif type == BlockType.HEADING:
            heading_type = ""
            num = 0
            for i in range(6, 0, -1):
                if block.startswith("#" * i):
                    heading_type = f"h{i}"
                    num = i
                    break
            text_nodes = text_to_textnodes(block[num:].strip())
            html_nodes = list(map(text_node_to_html_node, text_nodes))
            children.append(ParentNode(heading_type, html_nodes))
        elif type == BlockType.CODE:
            block = block[3:-3].strip()
            new_text = ""
            for line in block.split("\n"):
                new_text += f"{line.strip()}\n" if line else ""
            children.append(
                ParentNode(
                    "pre",
                    [LeafNode("code", new_text)],
                )
            )
        elif type == BlockType.QUOTE:
            block = " ".join(block.split())[1:].strip()
            text_nodes = text_to_textnodes(block)
            html_nodes = list(map(text_node_to_html_node, text_nodes))
            children.append(ParentNode("blockquote", html_nodes))

        elif type == BlockType.UNORDERED_LIST:
            items = []
            prev_line = ""
            for line in block.split("\n"):
                clean_line = " ".join(line.split())
                if not clean_line:
                    continue
                if clean_line.startswith("- "):
                    if prev_line:
                        text_nodes = text_to_textnodes(prev_line)
                        html_nodes = list(
                            map(
                                text_node_to_html_node,
                                text_nodes,
                            )
                        )
                        items.append(ParentNode("li", html_nodes))
                    prev_line = clean_line[2:]
                else:
                    prev_line += line
            if prev_line:
                text_nodes = text_to_textnodes(prev_line)
                html_nodes = list(map(text_node_to_html_node, text_nodes))
                items.append(ParentNode("li", html_nodes))
            children.append(ParentNode("ul", items))

        elif type == BlockType.ORDERED_LIST:
            items = []
            list_pos = 1
            prev_line = ""
            for line in block.split("\n"):
                clean_line = " ".join(line.split())
                if not clean_line:
                    continue
                list_num = f"{list_pos}. "
                if clean_line.startswith(list_num):
                    if prev_line:
                        text_nodes = text_to_textnodes(prev_line)
                        html_nodes = list(
                            map(
                                text_node_to_html_node,
                                text_nodes,
                            )
                        )
                        items.append(ParentNode("li", html_nodes))
                    i = len(list_num)
                    prev_line = clean_line[i:]
                    list_pos += 1
                else:
                    prev_line += line
            if prev_line:
                text_nodes = text_to_textnodes(prev_line)
                html_nodes = list(map(text_node_to_html_node, text_nodes))
                items.append(ParentNode("li", html_nodes))
            children.append(ParentNode("ol", items))
        else:
            raise Exception("Invalid block type")

    return ParentNode("div", children)
