"""
Generated from symbols.json for ::java::world::entity::mob::player::WardenSpawnTracker
Local link to file: generated_symbols/world/entity/mob/player/WardenSpawnTracker.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class WardenSpawnTracker(GeneratedModel):
    cooldown_ticks: Annotated[int, Field(ge=0)] | None = None  # Ticks before the `warning_level` can be increased again. Decreases by 1 every tick. It is set to 200 game ticks (10 seconds) every time the warning level is increased.
    ticks_since_last_warning: Annotated[int, Field(ge=0)] | None = None  # Ticks since the player was warned for warden spawning. Increases by 1 every tick. After 12000 game ticks (10 minutes) it will be set back to 0, and the `warning_level` will be decreased by 1.
    warning_level: Annotated[int, Field(ge=0, le=4)] | None = None  # The current warning level. The warden will spawn at level `4`.


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
                "desc": "The current warning level. The warden will spawn at level `4`.",
                "key": "warning_level",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 4
                    }
                },
                "optional": True
            }
        ]
    }
}

