"""
Generated from symbols.json for ::java::world::component::item::DebugStickState
Local link to file: vanilla_mcdoc/world/component/item/DebugStickState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownBlockId import KnownBlockId


type DebugStickState = dict[Annotated[str, IdSpec(registry='block')] | KnownBlockId, str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::DebugStickState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
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
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "mcdoc:block_state_keys"
                }
            }
        ]
    }
}
