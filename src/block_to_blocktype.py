from blocktype import BlockType
import re

def block_to_blocktype(block):
    if re.fullmatch(r'`{3}[\s\S]*?`{3}',block):
        return BlockType.CODE
    if len(block.split('\n'))==1:
        if re.match(r'^#{1,6} ',block):
            return BlockType.HEADING
    if block:
        start_with_larger_sign = True
        for line in block.split(sep='\n'):
            if not re.search(r'^\>',line):
                start_with_larger_sign = False
                break
        if start_with_larger_sign:
            return BlockType.QUOTE
    if block:
        start_with_hyphen = True
        for line in block.split(sep='\n'):
            if not re.search(r'^\- ',line):
                start_with_hyphen = False
                break
        if start_with_hyphen:
            return BlockType.UNORDERED_LIST
    if block:
        start_with_comma = True
        for num,line in enumerate(block.split(sep='\n')):
            found_number = re.search(r'^([\d]+)\. ',line)
            if not found_number or int(found_number.group(1))!=num+1:
                start_with_comma = False
                break
        if start_with_comma:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

    
