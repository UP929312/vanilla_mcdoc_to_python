"""
Generated from symbols.json for ::java::data::advancement::predicate::AxolotlPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/AxolotlPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.AxolotlVariant import AxolotlVariant


class AxolotlPredicate(GeneratedModel):
    variant: AxolotlVariant
