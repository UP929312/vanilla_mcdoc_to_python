"""
Generated from symbols.json for ::java::data::advancement::predicate::CatPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/CatPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class CatPredicate(GeneratedModel):
    variant: Annotated[str, IdSpec(registry='cat_variant', tags='allowed')] | list[Annotated[str, IdSpec(registry='cat_variant')]]
