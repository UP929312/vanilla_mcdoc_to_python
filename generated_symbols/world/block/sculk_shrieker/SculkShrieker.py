"""
Generated from symbols.json for ::java::world::block::sculk_shrieker::SculkShrieker
Local link to file: generated_symbols/world/block/sculk_shrieker/SculkShrieker.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.game_event.VibrationListener import VibrationListener


class SculkShrieker(GeneratedModel):
    warning_level: int | None = None
    listener: VibrationListener | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::sculk_shrieker::SculkShrieker": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "warning_level",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
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

