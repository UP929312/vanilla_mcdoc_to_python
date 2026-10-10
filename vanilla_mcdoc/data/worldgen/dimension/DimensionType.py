"""
Generated from symbols.json for ::java::data::worldgen::dimension::DimensionType
Local link to file: vanilla_mcdoc/data/worldgen/dimension/DimensionType.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.attribute.GlobalEnvironmentAttributeMap import GlobalEnvironmentAttributeMap
    from vanilla_mcdoc.data.worldgen.dimension.CardinalLightType import CardinalLightType
    from vanilla_mcdoc.data.worldgen.dimension.SkyboxType import SkyboxType
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class DimensionType(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dimension_type'

    attributes: GlobalEnvironmentAttributeMap | None = None
    default_clock: Annotated[str, IdSpec(registry='world_clock')] | None = None
    timelines: Annotated[str, IdSpec(registry='timeline', tags='allowed')] | list[Annotated[str, IdSpec(registry='timeline')]] | None = None
    has_skylight: bool  # Affects the weather, lighting engine and respawning rules.
    has_ceiling: bool  # Affects the weather, map items and respawning rules.
    has_ender_dragon_fight: bool
    coordinate_scale: Annotated[float, Field(ge=1e-05, le=30000000)]
    ambient_light: Annotated[float, Field(ge=0, le=1)]
    has_fixed_time: bool | None = None  # Defaults to `false`.
    logical_height: Annotated[int, Field(ge=0, le=4064)]  # Portals can't spawn and chorus fruit can't teleport players above this height.
    skybox: SkyboxType | None = None  # Skybox type. Defaults to `overworld`.
    cardinal_light: CardinalLightType | None = None  # The direction of cardinal lighting that affects blocks.
    infiniburn: Annotated[str, IdSpec(registry='block', tags='allowed')] | KnownBlockId | list[Annotated[str, IdSpec(registry='block')] | KnownBlockId]  # Defining what blocks keep fire infinitely burning.
    min_y: Annotated[int, Field(ge=-2032, le=2031), Field(multiple_of=16)]  # The minimum height in which blocks can exist.
    height: Annotated[int, Field(ge=16, le=4064), Field(multiple_of=16)]  # The total height in which blocks can exist. Max Y = Min Y + Height.
    monster_spawn_light_level: IntProvider[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)]
    monster_spawn_block_light_limit: Annotated[int, Field(ge=0, le=15)]
