"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AttachedToLogsTreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/AttachedToLogsTreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.util.direction.Direction import Direction


class AttachedToLogsTreeDecorator(GeneratedModel):
    probability: Annotated[float, Field(ge=0, le=1)]
    block_provider: BlockStateProvider
    directions: Annotated[list[Direction], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::AttachedToLogsTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "block_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "key": "directions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::direction::Direction"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

