# Generated from symbols.json for ::java::world::entity::mob::player::WardenSpawnTracker
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class WardenSpawnTracker:
    cooldown_ticks: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Ticks before the `warning_level` can be increased again. Decreases by 1 every tick. It is set to 200 game ticks (10 seconds) every time the warning level is increased.
    ticks_since_last_warning: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Ticks since the player was warned for warden spawning. Increases by 1 every tick. After 12000 game ticks (10 minutes) it will be set back to 0, and the `warning_level` will be decreased by 1.
    warning_level: Annotated[int, 'Range | `0`-`3` | both inclusive'] | None = None  # The warden will spawn at level 3.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::WardenSpawnTracker": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Ticks before the `warning_level` can be increased again.\nDecreases by 1 every tick. It is set to 200 game ticks (10 seconds) every time the warning level is increased.",
                "key": "cooldown_ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks since the player was warned for warden spawning.\nIncreases by 1 every tick. After 12000 game ticks (10 minutes) it will be set back to 0,\nand the `warning_level` will be decreased by 1.",
                "key": "ticks_since_last_warning",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The warden will spawn at level 3.",
                "key": "warning_level",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

