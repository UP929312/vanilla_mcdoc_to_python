"""
Generated from symbols.json for ::java::data::dispense_behavior::TransformBlock
Local link to file: vanilla_mcdoc/data/dispense_behavior/TransformBlock.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TransformBlock(GeneratedModel):
    transformer: Annotated[str, IdSpec(registry='block_transformer')]
