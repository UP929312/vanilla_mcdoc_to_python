"""
Generated from symbols.json for ::java::data::loot::function::CopyState
Local link to file: vanilla_mcdoc/data/loot/function/CopyState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class CopyState(Conditions):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: list[str]
