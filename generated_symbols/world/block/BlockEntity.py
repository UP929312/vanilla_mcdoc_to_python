"""
Generated from symbols.json for ::java::world::block::BlockEntity
Local link to file: generated_symbols/world/block/BlockEntity.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.world.component.DataComponentPatch import DataComponentPatch


@dataclass(kw_only=True)
class BlockEntity:
    id: Annotated[str, IdSpec(registry='block_entity_type')] | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None
    keepPacked: bool | None = None  # Unknown 0 for regular block entities
    components: DataComponentPatch | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::BlockEntity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block_entity_type"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "x",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "y",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "z",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Unknown\n0 for regular block entities",
                "key": "keepPacked",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPatch"
                },
                "optional": True
            }
        ]
    }
}

