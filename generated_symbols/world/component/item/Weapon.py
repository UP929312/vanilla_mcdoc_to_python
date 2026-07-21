# Generated from symbols.json for ::java::world::component::item::Weapon
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Weapon:
    item_damage_per_attack: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The amount to damage to the weapon item for each attack performed. Defaults to `1`.
    disable_blocking_for_seconds: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # If non-zero, will disable a blocking shield on successful attack for the specified amount of seconds.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Weapon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The amount to damage to the weapon item for each attack performed. Defaults to `1`.",
                "key": "item_damage_per_attack",
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
                "desc": "If non-zero, will disable a blocking shield on successful attack for the specified amount of seconds.",
                "key": "disable_blocking_for_seconds",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

