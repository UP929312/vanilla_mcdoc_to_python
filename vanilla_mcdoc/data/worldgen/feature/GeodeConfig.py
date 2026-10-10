"""
Generated from symbols.json for ::java::data::worldgen::feature::GeodeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/GeodeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.feature.GeodeBlockSettings import GeodeBlockSettings
    from vanilla_mcdoc.data.worldgen.feature.GeodeCrackSettings import GeodeCrackSettings
    from vanilla_mcdoc.data.worldgen.feature.GeodeLayerSettings import GeodeLayerSettings


class GeodeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    blocks: GeodeBlockSettings
    layers: GeodeLayerSettings
    crack: GeodeCrackSettings
    noise_multiplier: Annotated[float, Field(ge=0, le=1)] | None = None
    use_potential_placements_chance: Annotated[float, Field(ge=0, le=1)] | None = None
    use_alternate_layer0_chance: Annotated[float, Field(ge=0, le=1)] | None = None
    placements_require_layer0_alternate: bool | None = None
    outer_wall_distance: IntProvider[Annotated[int, Field(ge=1, le=20)]] | Annotated[int, Field(ge=1, le=20)] | None = None
    distribution_points: IntProvider[Annotated[int, Field(ge=1, le=20)]] | Annotated[int, Field(ge=1, le=20)] | None = None
    point_offset: IntProvider[Annotated[int, Field(ge=1, le=10)]] | Annotated[int, Field(ge=1, le=10)] | None = None
    min_gen_offset: int | None = None
    max_gen_offset: int | None = None
    invalid_blocks_threshold: int
