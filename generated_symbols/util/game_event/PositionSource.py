"""
Generated from symbols.json for ::java::util::game_event::PositionSource
Local link to file: generated_symbols/util/game_event/PositionSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal


@dataclass(kw_only=True)
class PositionSourceBlock:
    type: Literal['minecraft:block']
    pos: tuple[int, int, int]  # Block position


@dataclass(kw_only=True)
class PositionSourceEntity:
    type: Literal['minecraft:entity']
    source_entity: tuple[int, int, int, int]
    y_offset: float | None = None  # offset from the entity's feet to the source position


type PositionSource = PositionSourceBlock | PositionSourceEntity


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::game_event::PositionSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "position_source_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:position_source"
                }
            }
        ]
    }
}

