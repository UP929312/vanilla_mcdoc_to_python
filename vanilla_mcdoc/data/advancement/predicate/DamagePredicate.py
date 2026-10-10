"""
Generated from symbols.json for ::java::data::advancement::predicate::DamagePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/DamagePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate import DamageSourcePredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class DamagePredicate(GeneratedModel):
    dealt: MinMaxBounds[float] | float | None = None  # Amount of incoming damage before damage reduction.
    taken: MinMaxBounds[float] | float | None = None  # Amount of incoming damage after damage reduction.
    blocked: bool | None = None  # Whether the damage was successfully blocked.
    source_entity: EntityPredicate | None = None  # Source of the damage (eg: a skeleton shooting an arrow or player igniting tnt).
    type: DamageSourcePredicate | None = None
