"""
Generated from symbols.json for ::java::data::worldgen::feature::OreConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/OreConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.TargetBlock import TargetBlock


class OreConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    targets: list[TargetBlock]
    size: Annotated[int, Field(ge=0, le=64)]
    discard_chance_on_air_exposure: Annotated[float, Field(ge=0, le=1)]  # Chance that feature placement will be discarded if the ore is exposed to air blocks.
