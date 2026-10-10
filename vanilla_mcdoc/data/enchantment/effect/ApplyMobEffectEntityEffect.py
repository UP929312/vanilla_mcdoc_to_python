"""
Generated from symbols.json for ::java::data::enchantment::effect::ApplyMobEffectEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ApplyMobEffectEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class ApplyMobEffectEntityEffect(GeneratedModel):
    to_apply: Annotated[str, IdSpec(registry='mob_effect', tags='allowed')] | list[Annotated[str, IdSpec(registry='mob_effect')]]  # If multiple mob effects are specified, a random effect is selected.
    min_duration: LevelBasedValue
    max_duration: LevelBasedValue
    min_amplifier: LevelBasedValue
    max_amplifier: LevelBasedValue
