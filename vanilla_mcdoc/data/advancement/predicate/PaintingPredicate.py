"""
Generated from symbols.json for ::java::data::advancement::predicate::PaintingPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/PaintingPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class PaintingPredicate(GeneratedModel):
    variant: Annotated[str, IdSpec(registry='painting_variant', tags='allowed')] | list[Annotated[str, IdSpec(registry='painting_variant')]]
