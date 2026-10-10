"""
Generated from symbols.json for ::java::data::advancement::predicate::LocationPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/LocationPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.advancement.predicate.FluidPredicate import FluidPredicate
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class PositionStruct(GeneratedModel):
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None


class LightStruct(GeneratedModel):
    light: MinMaxBounds[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None


class LocationPredicate(GeneratedModel):
    position: PositionStruct | None = None
    biomes: Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/biome')]] | None = None
    structures: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]] | None = None
    dimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    light: LightStruct | None = None  # Calculated using: `max(sky-darkening, block)`.
    block: BlockPredicate | None = None
    fluid: FluidPredicate | None = None
    smokey: bool | None = None  # Whether the block is above (5 blocks or less) a campfire or soul campfire.
    can_see_sky: bool | None = None  # Whether the location has the maximum possible level of sky light
