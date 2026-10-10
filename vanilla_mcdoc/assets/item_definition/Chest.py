"""
Generated from symbols.json for ::java::assets::item_definition::Chest
Local link to file: vanilla_mcdoc/assets/item_definition/Chest.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ChestType import ChestType


class Chest(GeneratedModel):
    texture: Annotated[str, IdSpec(registry='texture', path='entity/chest/')]
    openness: Annotated[float, Field(ge=0, le=1)] | None = None  # Defaults to `0`.
    chest_type: ChestType | None = None  # Defaults to `single`.
