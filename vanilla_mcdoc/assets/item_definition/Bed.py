"""
Generated from symbols.json for ::java::assets::item_definition::Bed
Local link to file: vanilla_mcdoc/assets/item_definition/Bed.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.BedPart import BedPart


class Bed(GeneratedModel):
    texture: Annotated[str, IdSpec(registry='texture', path='entity/bed/')]
    part: BedPart
