"""
Generated from symbols.json for ::java::world::component::predicate::ContainerPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/ContainerPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate


class ContainerPredicate(GeneratedModel):
    items: CollectionPredicate[ItemPredicate] | None = None
