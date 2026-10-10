"""
Generated from symbols.json for ::java::data::advancement::predicate::EntitySlotsPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EntitySlotsPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate


type EntitySlotsPredicate = dict[str, ItemPredicate]
