"""
Generated from symbols.json for ::java::data::advancement::predicate::DamageSourcePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/DamageSourcePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate import DamageTagPredicate
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate


class DamageSourcePredicate(GeneratedModel):
    tags: list[DamageTagPredicate] | None = None  # Damage type tags that the damage type is in.
    source_entity: EntityPredicate | None = None  # Source of the damage (eg: a skeleton shooting an arrow or player igniting tnt).
    direct_entity: EntityPredicate | None = None  # Direct entity responsible for the damage (eg: the arrow or tnt).
    is_direct: bool | None = None  # Damage is direct when its direct and source entities are the same.
