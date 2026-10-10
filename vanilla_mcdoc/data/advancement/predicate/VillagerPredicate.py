"""
Generated from symbols.json for ::java::data::advancement::predicate::VillagerPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/VillagerPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class VillagerPredicate(GeneratedModel):
    variant: Annotated[str, IdSpec(registry='villager_type')]
