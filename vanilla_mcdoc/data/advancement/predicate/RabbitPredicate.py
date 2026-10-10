"""
Generated from symbols.json for ::java::data::advancement::predicate::RabbitPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/RabbitPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.RabbitVariant import RabbitVariant


class RabbitPredicate(GeneratedModel):
    variant: RabbitVariant
