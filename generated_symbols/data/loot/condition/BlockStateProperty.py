"""
Generated from symbols.json for ::java::data::loot::condition::BlockStateProperty
Local link to file: generated_symbols/data/loot/condition/BlockStateProperty.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId


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
