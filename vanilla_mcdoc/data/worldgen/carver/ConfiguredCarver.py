"""
Generated from symbols.json for ::java::data::worldgen::carver::ConfiguredCarver
Local link to file: vanilla_mcdoc/data/worldgen/carver/ConfiguredCarver.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.worldgen.carver.CanyonConfig import CanyonConfig
from vanilla_mcdoc.data.worldgen.carver.CaveConfig import CaveConfig


class ConfiguredCarverCanyon(CanyonConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/carver'

    type: Literal['minecraft:canyon', 'canyon'] = 'minecraft:canyon'


class ConfiguredCarverCave(CaveConfig):
    __resource_dir__: ClassVar[str] = 'worldgen/carver'

    type: Literal['minecraft:cave', 'cave'] = 'minecraft:cave'


type ConfiguredCarver = Annotated[
    Annotated[ConfiguredCarverCanyon, Tag('minecraft:canyon')]
    | Annotated[ConfiguredCarverCave, Tag('minecraft:cave')],
    Discriminator(tag_of('type')),
]
