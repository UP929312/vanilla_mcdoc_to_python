"""
Generated from symbols.json for ::java::data::loot::function::CopyState
Local link to file: generated_symbols/data/loot/function/CopyState.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId


@dataclass(kw_only=True)
class CopyState(Conditions):
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: list[str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyState": {
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
                    "kind": "list",
                    "item": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "dynamic",
                                "accessor": [
                                    {
                                        "keyword": "parent"
                                    },
                                    "block"
                                ]
                            }
                        ],
                        "registry": "mcdoc:block_state_keys"
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

