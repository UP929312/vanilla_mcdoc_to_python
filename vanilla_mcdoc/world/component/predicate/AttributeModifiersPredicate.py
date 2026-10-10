"""
Generated from symbols.json for ::java::world::component::predicate::AttributeModifiersPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/AttributeModifiersPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicateEntry import AttributeModifiersPredicateEntry
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate


class AttributeModifiersPredicate(GeneratedModel):
    modifiers: CollectionPredicate[AttributeModifiersPredicateEntry] | None = None
