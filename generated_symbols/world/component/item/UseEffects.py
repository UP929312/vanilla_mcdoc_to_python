# Generated from symbols.json for ::java::world::component::item::UseEffects
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class UseEffects:
    can_sprint: bool | None = None  # Whether the player can sprint while using this item. Defaults to `false`.
    speed_multiplier: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # The speed multiplier applied to the player while using this item. Defaults to 0.2
    interact_vibrations: bool | None = None  # Whether using this item emits game events (`item_interact_start` and `item_interact_finish`). Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::UseEffects": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Whether the player can sprint while using this item.\nDefaults to `False`.",
                "key": "can_sprint",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The speed multiplier applied to the player while using this item.\nDefaults to 0.2",
                "key": "speed_multiplier",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether using this item emits game events (`item_interact_start` and `item_interact_finish`).\nDefaults to `True`.",
                "key": "interact_vibrations",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

