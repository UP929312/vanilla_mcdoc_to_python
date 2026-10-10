"""
Generated from symbols.json for ::java::data::worldgen::structure::NetherFossil
Local link to file: vanilla_mcdoc/data/worldgen/structure/NetherFossil.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.HeightProvider import HeightProvider


class NetherFossil(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    height: HeightProvider
