"""
Generated from symbols.json for ::java::util::block_state::FullBlockState
Local link to file: generated_symbols/util/block_state/FullBlockState.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownBlockId import KnownBlockId


class FullBlockState(GeneratedModel):
    id: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: dict[str, str] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::block_state::FullBlockState": {
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
                                "id"
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
