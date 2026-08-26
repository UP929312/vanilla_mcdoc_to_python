"""
Generated from symbols.json for ::java::util::game_event::PositionSource
Local link to file: generated_symbols/util/game_event/PositionSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.util.game_event.BlockPositionSource import BlockPositionSource
from generated_symbols.util.game_event.EntityPositionSource import EntityPositionSource


@dataclass(kw_only=True)
class PositionSourceBlock(BlockPositionSource):
    type: Literal['minecraft:block']


@dataclass(kw_only=True)
class PositionSourceEntity(EntityPositionSource):
    type: Literal['minecraft:entity']


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

