"""
Generated from symbols.json for ::java::data::advancement::predicate::TropicalFishPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/TropicalFishPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.TropicalFishPattern import TropicalFishPattern


class TropicalFishPredicate(GeneratedModel):
    variant: TropicalFishPattern
