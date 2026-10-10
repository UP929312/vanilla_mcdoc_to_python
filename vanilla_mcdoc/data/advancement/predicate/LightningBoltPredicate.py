"""
Generated from symbols.json for ::java::data::advancement::predicate::LightningBoltPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/LightningBoltPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class LightningBoltPredicate(GeneratedModel):
    blocks_set_on_fire: MinMaxBounds[int] | int | None = None
    entity_struck: EntityPredicate | None = None
