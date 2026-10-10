"""
Generated from symbols.json for ::java::data::enchantment::effect::ReplaceBlockEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/ReplaceBlockEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class ReplaceBlockEntityEffect(GeneratedModel):
    block_state: BlockStateProviderRef
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the placed block by. Defaults to `[0, 0, 0]`.
    predicate: BlockPredicate | None = None  # If omitted, all block types are replaced.
    trigger_game_event: Annotated[str, IdSpec(registry='game_event')] | None = None  # Defaults to no game event dispatched.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ReplaceBlockEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Relative coordinates to offset the placed block by. Defaults to `[0, 0, 0]`.",
                "key": "offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, all block types are replaced.",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to no game event dispatched.",
                "key": "trigger_game_event",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "game_event"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
