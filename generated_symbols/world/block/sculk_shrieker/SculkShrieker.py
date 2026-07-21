# Generated from symbols.json for ::java::world::block::sculk_shrieker::SculkShrieker
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.game_event.VibrationListener import VibrationListener


@dataclass(kw_only=True)
class SculkShrieker:
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

