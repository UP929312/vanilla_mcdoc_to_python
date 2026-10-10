"""
Generated from symbols.json for ::java::data::advancement::predicate::FrogPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/FrogPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class FrogPredicate(GeneratedModel):
    variant: Annotated[str, IdSpec(registry='frog_variant', tags='allowed')] | list[Annotated[str, IdSpec(registry='frog_variant')]]
