"""
Generated from symbols.json for ::java::data::worldgen::feature::NetherForestVegetationConfig
Local link to file: generated_symbols/data/worldgen/feature/NetherForestVegetationConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class NetherForestVegetationConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state_provider: BlockStateProviderRef
    spread_width: Annotated[int, Field(ge=1)]
    spread_height: Annotated[int, Field(ge=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::NetherForestVegetationConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "spread_width",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "spread_height",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

