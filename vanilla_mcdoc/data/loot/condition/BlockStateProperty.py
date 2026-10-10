"""
Generated from symbols.json for ::java::data::loot::condition::BlockStateProperty
Local link to file: vanilla_mcdoc/data/loot/condition/BlockStateProperty.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


class BlockStateProperty(GeneratedModel):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: dict[str, str] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::BlockStateProperty": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "properties",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "block"
                            ]
                        }
                    ],
                    "registry": "mcdoc:block_states"
                },
                "optional": True
            }
        ]
    }
}
