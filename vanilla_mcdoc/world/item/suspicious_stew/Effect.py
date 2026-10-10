"""
Generated from symbols.json for ::java::world::item::suspicious_stew::Effect
Local link to file: vanilla_mcdoc/world/item/suspicious_stew/Effect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.EffectId import EffectId


class Effect(GeneratedModel):
    EffectId_: EffectId | None = Field(default=None, alias='EffectId')
    EffectDuration: Annotated[int, Field(ge=1)] | None = None  # Duration in ticks.
