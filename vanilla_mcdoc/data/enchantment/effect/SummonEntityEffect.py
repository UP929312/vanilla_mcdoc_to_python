"""
Generated from symbols.json for ::java::data::enchantment::effect::SummonEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/SummonEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class SummonEntityEffect(GeneratedModel):
    entity: Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]]  # If multiple entity types are specified, a random entity type is selected.
    join_team: bool | None = None  # Whether the summoned entity should join the team of the owner of the Enchanted Item.
