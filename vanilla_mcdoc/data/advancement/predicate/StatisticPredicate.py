"""
Generated from symbols.json for ::java::data::advancement::predicate::StatisticPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/StatisticPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class StatisticPredicateBroken(GeneratedModel):
    type: Literal['minecraft:broken', 'broken'] = 'minecraft:broken'
    stat: Annotated[str, IdSpec(registry='item')] | KnownItemId
    value: MinMaxBounds[int] | int


class StatisticPredicateCrafted(GeneratedModel):
    type: Literal['minecraft:crafted', 'crafted'] = 'minecraft:crafted'
    stat: Annotated[str, IdSpec(registry='item')] | KnownItemId
    value: MinMaxBounds[int] | int


class StatisticPredicateCustom(GeneratedModel):
    type: Literal['minecraft:custom', 'custom'] = 'minecraft:custom'
    stat: Annotated[str, IdSpec(registry='custom_stat')]
    value: MinMaxBounds[int] | int


class StatisticPredicateDropped(GeneratedModel):
    type: Literal['minecraft:dropped', 'dropped'] = 'minecraft:dropped'
    stat: Annotated[str, IdSpec(registry='item')] | KnownItemId
    value: MinMaxBounds[int] | int


class StatisticPredicateKilled(GeneratedModel):
    type: Literal['minecraft:killed', 'killed'] = 'minecraft:killed'
    stat: Annotated[str, IdSpec(registry='entity_type')]
    value: MinMaxBounds[int] | int


class StatisticPredicateKilledBy(GeneratedModel):
    type: Literal['minecraft:killed_by', 'killed_by'] = 'minecraft:killed_by'
    stat: Annotated[str, IdSpec(registry='entity_type')]
    value: MinMaxBounds[int] | int


class StatisticPredicateMined(GeneratedModel):
    type: Literal['minecraft:mined', 'mined'] = 'minecraft:mined'
    stat: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    value: MinMaxBounds[int] | int


class StatisticPredicatePickedUp(GeneratedModel):
    type: Literal['minecraft:picked_up', 'picked_up'] = 'minecraft:picked_up'
    stat: Annotated[str, IdSpec(registry='item')] | KnownItemId
    value: MinMaxBounds[int] | int


class StatisticPredicateUsed(GeneratedModel):
    type: Literal['minecraft:used', 'used'] = 'minecraft:used'
    stat: Annotated[str, IdSpec(registry='item')] | KnownItemId
    value: MinMaxBounds[int] | int


type StatisticPredicate = Annotated[
    Annotated[StatisticPredicateBroken, Tag('minecraft:broken')]
    | Annotated[StatisticPredicateCrafted, Tag('minecraft:crafted')]
    | Annotated[StatisticPredicateCustom, Tag('minecraft:custom')]
    | Annotated[StatisticPredicateDropped, Tag('minecraft:dropped')]
    | Annotated[StatisticPredicateKilled, Tag('minecraft:killed')]
    | Annotated[StatisticPredicateKilledBy, Tag('minecraft:killed_by')]
    | Annotated[StatisticPredicateMined, Tag('minecraft:mined')]
    | Annotated[StatisticPredicatePickedUp, Tag('minecraft:picked_up')]
    | Annotated[StatisticPredicateUsed, Tag('minecraft:used')],
    Discriminator(tag_of('type')),
]
