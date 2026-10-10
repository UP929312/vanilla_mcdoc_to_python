"""
Generated from symbols.json for ::java::data::advancement::predicate::WolfPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/WolfPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class WolfPredicate(GeneratedModel):
    variant: Annotated[str, IdSpec(registry='wolf_variant', tags='allowed')] | list[Annotated[str, IdSpec(registry='wolf_variant')]]
