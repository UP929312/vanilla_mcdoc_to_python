"""
Generated from symbols.json for ::java::data::loot::condition::BlockStateProperty
Local link to file: generated_symbols/data/loot/condition/BlockStateProperty.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId


type PropertiesStructBlockStatesNone = dict[str, str]


@dataclass(kw_only=True)
class BlockStateProperty:
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: PropertiesStructBlockStatesNone | None = None


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

