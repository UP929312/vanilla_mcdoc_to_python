"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::ContactDamage
Local link to file: vanilla_mcdoc/data/sulfur_cube_archetype/ContactDamage.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider


class ContactDamage(GeneratedModel):
    damage_type: Annotated[str, IdSpec(registry='damage_type')]
    amount: FloatProvider[Annotated[float, Field(ge=0)]] | Annotated[float, Field(ge=0)]
    attribute_to_source: bool  # Whether the damage is attributed to the sulfur cube.
