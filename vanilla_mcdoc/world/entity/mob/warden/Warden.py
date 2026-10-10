"""
Generated from symbols.json for ::java::world::entity::mob::warden::Warden
Local link to file: vanilla_mcdoc/world/entity/mob/warden/Warden.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.game_event.VibrationListener import VibrationListener
    from vanilla_mcdoc.world.entity.mob.warden.AngerManagement import AngerManagement


class Warden(MobBase):
    anger: AngerManagement | None = None  # Anger management
    listener: VibrationListener | None = None  # Vibration listener
