"""
Generated from symbols.json for ::java::data::advancement::predicate::MooshroomPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/MooshroomPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.MooshroomType import MooshroomType


class MooshroomPredicate(GeneratedModel):
    variant: MooshroomType
