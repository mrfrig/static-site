from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str):
    if re.fullmatch(r"#{1,6} .+", block):
        return BlockType.HEADING
    if len(block) >= 6 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    is_ordered_list = True
    list_pos = 1
    for line in block.split("\n"):
        if not line.startswith(f"{list_pos}. "):
            is_ordered_list = False
            break
        list_pos += 1
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
