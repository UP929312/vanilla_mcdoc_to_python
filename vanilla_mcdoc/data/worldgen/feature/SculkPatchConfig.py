"""
Generated from symbols.json for ::java::data::worldgen::feature::SculkPatchConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SculkPatchConfig.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class SculkPatchConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    charge_count: Annotated[int, Field(ge=1, le=32)]
    amount_per_charge: Annotated[int, Field(ge=1, le=500)]
    spread_attempts: Annotated[int, Field(ge=1, le=64)]
    growth_rounds: Annotated[int, Field(ge=0, le=8)]
    spread_rounds: Annotated[int, Field(ge=0, le=8)]
