"""
Generated from symbols.json for ::java::data::worldgen::structure::Mineshaft
Local link to file: vanilla_mcdoc/data/worldgen/structure/Mineshaft.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.MineshaftType import MineshaftType


class Mineshaft(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    mineshaft_type: MineshaftType
