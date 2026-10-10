"""
Generated from symbols.json for ::java::data::advancement::predicate::BoatPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/BoatPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.boat.BoatType import BoatType


class BoatPredicate(GeneratedModel):
    variant: BoatType
