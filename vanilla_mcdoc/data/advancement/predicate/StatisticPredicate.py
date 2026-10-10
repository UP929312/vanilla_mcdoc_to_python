"""
Generated from symbols.json for ::java::data::advancement::predicate::StatisticPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/StatisticPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class StatisticPredicate(GeneratedModel):
    type: Annotated[str, IdSpec(registry='stat_type')]
    stat: str | Annotated[str, IdSpec(registry='item')] | KnownItemId | Annotated[str, IdSpec(registry='custom_stat')] | Annotated[str, IdSpec(registry='entity_type')] | Annotated[str, IdSpec(registry='block')] | KnownBlockId
    value: MinMaxBounds[int] | int
