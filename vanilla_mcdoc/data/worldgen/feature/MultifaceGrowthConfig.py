"""
Generated from symbols.json for ::java::data::worldgen::feature::MultifaceGrowthConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/MultifaceGrowthConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.MultifaceBlock import MultifaceBlock
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class MultifaceGrowthConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: MultifaceBlock
    search_range: Annotated[int, Field(ge=1, le=64)] | None = None
    chance_of_spreading: Annotated[float, Field(ge=0, le=1)] | None = None
    can_place_on_floor: bool | None = None
    can_place_on_ceiling: bool | None = None
    can_place_on_wall: bool | None = None
    can_be_placed_on: list[Annotated[str, IdSpec(registry='block')] | KnownBlockId] | Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | None = None
