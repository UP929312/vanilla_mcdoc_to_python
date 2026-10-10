"""
Generated from symbols.json for ::java::util::effect::OldMobEffect
Local link to file: vanilla_mcdoc/util/effect/OldMobEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.EffectId import EffectId
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance


class OldMobEffect(GeneratedModel):
    Id: EffectId | None = None
    Amplifier: int | Annotated[int, Field(ge=0, le=255)] | None = None
    Duration: Annotated[int, Field(ge=1)] | Literal[-1] | None = None  # Duration of the effect in ticks. Infinite is represented by `-1`.
    Ambient: bool | None = None  # Whether particles are semi-transparent. (like with a Beacon)
    ShowParticles: bool | None = None  # Whether particles should be shown.
    ShowIcon: bool | None = None  # Whether the effect icon should be shown.
    HiddenEffect: MobEffectInstance | None = None  # A lower amplifier effect of the same type.
