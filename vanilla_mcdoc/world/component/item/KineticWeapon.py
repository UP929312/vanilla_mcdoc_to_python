"""
Generated from symbols.json for ::java::world::component::item::KineticWeapon
Local link to file: vanilla_mcdoc/world/component/item/KineticWeapon.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.world.component.item.KineticWeaponEffectCondition import KineticWeaponEffectCondition


class KineticWeapon(GeneratedModel):
    delay_ticks: Annotated[int, Field(ge=0)] | None = None  # The time in ticks required for charging. Defaults to 0
    contact_cooldown_ticks: Annotated[int, Field(ge=0)] | None = None  # The cooldown in ticks after hitting, and loosing contact with an entity before being able to hit it again Defaults to 10
    dismount_conditions: KineticWeaponEffectCondition | None = None
    knockback_conditions: KineticWeaponEffectCondition | None = None
    damage_conditions: KineticWeaponEffectCondition | None = None
    forward_movement: float | None = None  # The distance the item moves out of hand during animation. Defaults to 0.0
    damage_multiplier: float | None = None  # The multiplier for the final damage from the relative speed. Defaults to 1.0
    sound: SoundEventRef | None = None  # Sound to play when the weapon is engaged.
    hit_sound: SoundEventRef | None = None  # Sound to play when the weapon hits an entity.
