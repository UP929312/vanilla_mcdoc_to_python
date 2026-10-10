"""
Generated from symbols.json for ::java::data::advancement::predicate::FoxPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/FoxPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.FoxType import FoxType


class FoxPredicate(GeneratedModel):
    variant: FoxType
