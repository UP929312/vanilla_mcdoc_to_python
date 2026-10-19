"""
Generated from symbols.json for ::java::data::block_transformer::BlockTransformer
Local link to file: vanilla_mcdoc/data/block_transformer/BlockTransformer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.data.block_transformer.BlockTransformData import BlockTransformData


type BlockTransformer = Annotated[list[BlockTransformData], Field(min_length=1, max_length=200)]
