"""
Generated from symbols.json for ::java::data::advancement::predicate::DamageTagPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/DamageTagPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class DamageTagPredicate(GeneratedModel):
    id: Annotated[str, IdSpec(registry='damage_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='damage_type')]]
    expected: bool  # Whether the damage is expected to have or not have the tag.
