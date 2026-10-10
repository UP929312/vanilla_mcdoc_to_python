"""
Generated from symbols.json for ::java::data::loot::function::FillPlayerHead
Local link to file: vanilla_mcdoc/data/loot/function/FillPlayerHead.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


class FillPlayerHead(Conditions):
    entity: EntityTarget  # `this` to use the entity that died or the player that gained the advancement, opened the container, or broke the block.
