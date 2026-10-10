"""
Generated from symbols.json for ::java::util::effect::MobEffectInstance
Local link to file: vanilla_mcdoc/util/effect/MobEffectInstance.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class MobEffectInstance(GeneratedModel):
    id: Annotated[str, IdSpec(registry='mob_effect')]
    amplifier: int | Annotated[int, Field(ge=0, le=255)] | None = None  # Level I having value 0. Defaults to 0.
    duration: Literal[-1] | Annotated[int, Field(ge=1)] | None = None  # Duration of the effect in ticks. Infinite is represented by `-1`.
    ambient: bool | None = None  # Whether the effect appears as a HUD icon in addition to in the inventory GUI (same behavior as beacons when `true`). Defaults to `false`.
    show_particles: bool | None = None  # Defaults to `true`.
    show_icon: bool | None = None  # Whether the effect appears in the inventory GUI. Defaults to `true`
    hidden_effect: MobEffectInstance | None = None  # A lower amplifier effect of the same type.
