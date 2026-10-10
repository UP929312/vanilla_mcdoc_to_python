"""
Generated from symbols.json for ::java::data::worldgen::feature::TemplateEntry
Local link to file: vanilla_mcdoc/data/worldgen/feature/TemplateEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.Rotation import Rotation


class TemplateEntry(GeneratedModel):
    id: Annotated[str, IdSpec(registry='structure')]  # The structure template to place.
    rotations: list[Rotation] | None = None  # Rotations to choose from and apply to this template, centered around the origin. If not specified, defaults to all allowed rotations.
