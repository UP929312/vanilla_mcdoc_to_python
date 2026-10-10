"""
Generated from symbols.json for ::java::world::component::item::Weapon
Local link to file: vanilla_mcdoc/world/component/item/Weapon.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class Weapon(GeneratedModel):
    item_damage_per_attack: Annotated[int, Field(ge=0)] | None = None  # The amount to damage to the weapon item for each attack performed. Defaults to `1`.
    disable_blocking_for_seconds: Annotated[float, Field(ge=0)] | None = None  # If non-zero, will disable a blocking shield on successful attack for the specified amount of seconds.


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
