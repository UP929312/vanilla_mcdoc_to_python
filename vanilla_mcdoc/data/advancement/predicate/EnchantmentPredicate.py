"""
Generated from symbols.json for ::java::data::advancement::predicate::EnchantmentPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EnchantmentPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class EnchantmentPredicate(GeneratedModel):
    enchantments: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None
    levels: MinMaxBounds[int] | int | None = None
