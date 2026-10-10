"""
Generated from symbols.json for ::java::world::item::Enchantment
Local link to file: vanilla_mcdoc/world/item/Enchantment.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Enchantment(GeneratedModel):
    id: Annotated[str, IdSpec(registry='enchantment')] | None = None  # Which enchantment is being described.
    lvl: Annotated[int, Field(ge=0, le=255)] | None = None  # Which level the enchantment is.
