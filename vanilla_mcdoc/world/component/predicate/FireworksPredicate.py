"""
Generated from symbols.json for ::java::world::component::predicate::FireworksPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/FireworksPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate
    from vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate


class FireworksPredicate(GeneratedModel):
    explosions: CollectionPredicate[FireworkExplosionPredicate] | None = None
    flight_duration: MinMaxBounds[int] | int | None = None
