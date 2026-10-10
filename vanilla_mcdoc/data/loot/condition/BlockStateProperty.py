"""
Generated from symbols.json for ::java::data::loot::condition::BlockStateProperty
Local link to file: vanilla_mcdoc/data/loot/condition/BlockStateProperty.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class BlockStateProperty(GeneratedModel):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: dict[str, str] | None = None
