"""
Generated from symbols.json for ::java::data::enchantment::effect::AllOfEffectValue
Local link to file: vanilla_mcdoc/data/enchantment/effect/AllOfEffectValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.effect.ValueEffect import ValueEffect


class AllOfEffectValue(GeneratedModel):
    effects: Annotated[list[ValueEffect], Field(min_length=1)]
