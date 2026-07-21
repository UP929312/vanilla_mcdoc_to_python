# Generated from symbols.json for ::java::data::loot::function::SetFireworks
from dataclasses import dataclass
from typing import Annotated, Any
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class SetFireworks(Conditions):
    flight_duration: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.
    explosions: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetFireworks": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.",
                "key": "flight_duration",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "explosions",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "values",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "static",
                                            "value": "firework_explosion"
                                        }
                                    ],
                                    "registry": "minecraft:data_component"
                                }
                            }
                        },
                        {
                            "kind": "spread",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::loot::function::ListOperation"
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

