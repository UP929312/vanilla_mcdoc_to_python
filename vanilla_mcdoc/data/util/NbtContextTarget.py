"""
Generated from symbols.json for ::java::data::util::NbtContextTarget
Local link to file: vanilla_mcdoc/data/util/NbtContextTarget.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.BlockEntityTarget import BlockEntityTarget
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


type NbtContextTarget = EntityTarget | BlockEntityTarget
