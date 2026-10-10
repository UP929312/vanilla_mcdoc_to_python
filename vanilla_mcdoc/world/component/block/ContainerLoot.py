"""
Generated from symbols.json for ::java::world::component::block::ContainerLoot
Local link to file: vanilla_mcdoc/world/component/block/ContainerLoot.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class ContainerLoot(GeneratedModel):
    loot_table: Annotated[str, IdSpec(registry='loot_table')]
    seed: int | None = None
