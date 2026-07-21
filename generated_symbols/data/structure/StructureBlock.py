# Generated from symbols.json for ::java::data::structure::StructureBlock
from dataclasses import dataclass
from typing import Annotated, Any


@dataclass(kw_only=True)
class StructureBlock:
    state: Annotated[int, 'Range | Min `0` and above | inclusive']
    pos: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    nbt: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::StructureBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 0
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "nbt",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "%fallback"
                        }
                    ],
                    "registry": "minecraft:block"
                },
                "optional": True
            }
        ]
    }
}

