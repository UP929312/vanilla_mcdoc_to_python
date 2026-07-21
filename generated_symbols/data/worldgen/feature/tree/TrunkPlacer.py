# Generated from symbols.json for ::java::data::worldgen::feature::tree::TrunkPlacer
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TrunkPlacer:
    type: str
    base_height: Annotated[int, 'Range | `0`-`32` | both inclusive']
    height_rand_a: Annotated[int, 'Range | `0`-`24` | both inclusive']
    height_rand_b: Annotated[int, 'Range | `0`-`24` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TrunkPlacer": {
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
                                    "value": "worldgen/trunk_placer_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "base_height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 32
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height_rand_a",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 24
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height_rand_b",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 24
                    }
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
                    "registry": "minecraft:trunk_placer"
                }
            }
        ]
    }
}

