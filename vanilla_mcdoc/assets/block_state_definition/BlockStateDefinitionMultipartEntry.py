"""
Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionMultipartEntry
Local link to file: vanilla_mcdoc/assets/block_state_definition/BlockStateDefinitionMultipartEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.block_state_definition.ModelVariant import ModelVariant
    from vanilla_mcdoc.assets.block_state_definition.MultiPartCondition import MultiPartCondition


class BlockStateDefinitionMultipartEntry(GeneratedModel):
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.
    apply: ModelVariant
