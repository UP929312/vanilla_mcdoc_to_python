# Generated from symbols.json for ::java::world::entity::mob::warden::Warden
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from generated_symbols.util.game_event.VibrationListener import VibrationListener
    from generated_symbols.world.entity.mob.warden.AngerManagement import AngerManagement


@dataclass(kw_only=True)
class Warden(MobBase):
    anger: AngerManagement | None = None  # Anger management
    listener: VibrationListener | None = None  # Vibration listener


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::warden::Warden": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Anger management",
                "key": "anger",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::warden::AngerManagement"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Vibration listener",
                "key": "listener",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::game_event::VibrationListener"
                },
                "optional": True
            }
        ]
    }
}

