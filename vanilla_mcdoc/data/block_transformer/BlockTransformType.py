"""
Generated from symbols.json for ::java::data::block_transformer::BlockTransformType
Local link to file: vanilla_mcdoc/data/block_transformer/BlockTransformType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class BlockTransformType(StrEnum):
    SINGLEBLOCK = "single_block"
    COPPERCHEST = "copper_chest"  # If the original block and the transformed block are both copper chests of any kind, the transform applies to the other half of the double chest.
