"""
Generated from symbols.json for ::java::world::component::item::PiercingWeapon
Local link to file: vanilla_mcdoc/world/component/item/PiercingWeapon.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class PiercingWeapon(GeneratedModel):
    deals_knockback: bool | None = None  # Whether the attack deals knockback. Defaults to `true`.
    dismounts: bool | None = None  # Whether the attack dismounts the target. Defaults to `false`.
    sound: SoundEventRef | None = None  # Sound to play when using the weapon to attack.
    hit_sound: SoundEventRef | None = None  # Sound to play when the weapon hits an entity.
