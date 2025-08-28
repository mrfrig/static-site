from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    block = block.lstrip()
    if re.fullmatch(r"#{1,6} .+", block):
        return BlockType.HEADING
    if len(block) >= 6 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
