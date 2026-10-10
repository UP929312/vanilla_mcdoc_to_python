"""
Generated from symbols.json for ::java::data::advancement::predicate::ItemPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/ItemPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId
    from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from vanilla_mcdoc.world.component.DataComponentPredicate import DataComponentPredicate


class ItemPredicate(GeneratedModel):
    items: Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId] | None = None
    count: MinMaxBounds[int] | int | None = None
    components: DataComponentExactPredicate | None = None
    predicates: DataComponentPredicate | None = None
