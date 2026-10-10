"""
Generated from symbols.json for ::java::data::advancement::predicate::HorsePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/HorsePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.HorseVariant import HorseVariant


class HorsePredicate(GeneratedModel):
    variant: HorseVariant
