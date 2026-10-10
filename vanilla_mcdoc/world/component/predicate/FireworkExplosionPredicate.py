"""
Generated from symbols.json for ::java::world::component::predicate::FireworkExplosionPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/FireworkExplosionPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.FireworkShape import FireworkShape


class FireworkExplosionPredicate(GeneratedModel):
    shape: FireworkShape | None = None
    has_twinkle: bool | None = None
    has_trail: bool | None = None
