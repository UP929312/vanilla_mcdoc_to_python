"""
Generated from symbols.json for ::java::data::enchantment::effect::SetBlockPropertiesEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/SetBlockPropertiesEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class SetBlockPropertiesEntityEffect(GeneratedModel):
    properties: dict[str, str]
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the block by. Defaults to `[0, 0, 0]`.
    trigger_game_event: Annotated[str, IdSpec(registry='game_event')] | None = None  # Defaults to no game event dispatched.


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
