"""
Generated from symbols.json for ::java::data::advancement::AdvancementIcon
Local link to file: vanilla_mcdoc/data/advancement/AdvancementIcon.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class AdvancementIcon(GeneratedModel):
    item: Annotated[str, IdSpec(registry='item')] | KnownItemId
    nbt: str | None = None
