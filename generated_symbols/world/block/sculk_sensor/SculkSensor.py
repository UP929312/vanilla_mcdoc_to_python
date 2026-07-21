# Generated from symbols.json for ::java::world::block::sculk_sensor::SculkSensor
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.game_event.VibrationListener import VibrationListener


@dataclass(kw_only=True)
class SculkSensor:
    last_vibration_frequency: Annotated[int, 'Range | `1`-`15` | both inclusive'] | None = None
    listener: VibrationListener | None = None  # Vibration listener


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::sculk_sensor::SculkSensor": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "last_vibration_frequency",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 15
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
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

