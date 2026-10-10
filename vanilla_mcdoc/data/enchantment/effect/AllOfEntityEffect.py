"""
Generated from symbols.json for ::java::data::enchantment::effect::AllOfEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/AllOfEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.EntityEffect import EntityEffect


class AllOfEntityEffect(GeneratedModel):
    effects: Annotated[list[EntityEffect], Field(min_length=1)]
