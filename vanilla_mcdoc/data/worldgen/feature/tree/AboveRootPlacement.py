"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::AboveRootPlacement
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/AboveRootPlacement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class AboveRootPlacement(GeneratedModel):
    above_root_provider: BlockStateProviderRef
    above_root_placement_chance: Annotated[float, Field(ge=0, le=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::AboveRootPlacement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "above_root_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "above_root_placement_chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}
