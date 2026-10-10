"""
Generated from symbols.json for ::java::data::advancement::predicate::MobEffectPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/MobEffectPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class MobEffectPredicate(GeneratedModel):
    amplifier: MinMaxBounds[int] | int | None = None
    duration: MinMaxBounds[int] | int | None = None
    ambient: bool | None = None
    visible: bool | None = None
