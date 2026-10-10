"""
Generated from symbols.json for ::java::world::component::item::FoodEffect
Local link to file: vanilla_mcdoc/world/component/item/FoodEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance


class FoodEffect(GeneratedModel):
    effect: MobEffectInstance
    probability: Annotated[float, Field(ge=0, le=1)] | None = None  # Chance for the effect to be applied. Defaults to 1.
