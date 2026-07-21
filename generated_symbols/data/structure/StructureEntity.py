# Generated from symbols.json for ::java::data::structure::StructureEntity
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class StructureEntity:
    pos: tuple[Annotated[float, 'Range | Min `0` and above | inclusive'], Annotated[float, 'Range | Min `0` and above | inclusive'], Annotated[float, 'Range | Min `0` and above | inclusive']]
    blockPos: tuple[Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive'], Annotated[int, 'Range | Min `0` and above | inclusive']]
    nbt: AnyEntity


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::StructureEntity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "double",
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
                "key": "blockPos",
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
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            }
        ]
    }
}

