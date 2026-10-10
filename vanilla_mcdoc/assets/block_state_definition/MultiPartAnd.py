"""
Generated from symbols.json for ::java::assets::block_state_definition::MultiPartAnd
Local link to file: vanilla_mcdoc/assets/block_state_definition/MultiPartAnd.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.block_state_definition.MultiPartCondition import MultiPartCondition


class MultiPartAnd(GeneratedModel):
    AND: list[MultiPartCondition]
