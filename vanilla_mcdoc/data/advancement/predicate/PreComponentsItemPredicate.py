"""
Generated from symbols.json for ::java::data::advancement::predicate::PreComponentsItemPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/PreComponentsItemPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class PreComponentsItemPredicate(GeneratedModel):
    items: list[Annotated[str, IdSpec(registry='item')] | KnownItemId] | None = None
    tag: Annotated[str, IdSpec(registry='item', tags='implicit')] | KnownItemId | None = None
    durability: MinMaxBounds[int] | int | None = None
    potion: Annotated[str, IdSpec(registry='potion')] | None = None
    enchantments: list[EnchantmentPredicate] | None = None
    stored_enchantments: list[EnchantmentPredicate] | None = None
    nbt: str | None = None
