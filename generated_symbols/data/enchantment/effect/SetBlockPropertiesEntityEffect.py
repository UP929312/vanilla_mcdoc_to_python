# Generated from symbols.json for ::java::data::enchantment::effect::SetBlockPropertiesEntityEffect
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class SetBlockPropertiesEntityEffect:
    properties: Any
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the block by. Defaults to `[0, 0, 0]`.
    trigger_game_event: str | None = None  # Defaults to no game event dispatched.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::SetBlockPropertiesEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "properties",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "block_state"
                        }
                    ],
                    "registry": "minecraft:data_component"
                }
            },
            {
                "kind": "pair",
                "desc": "Relative coordinates to offset the block by. Defaults to `[0, 0, 0]`.",
                "key": "offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to no game event dispatched.",
                "key": "trigger_game_event",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "game_event"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

