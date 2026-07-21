# Generated from symbols.json for ::java::data::worldgen::feature::tree::AboveRootPlacement
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class AboveRootPlacement:
    above_root_provider: BlockStateProvider
    above_root_placement_chance: Annotated[float, 'Range | `0`-`1` | both inclusive']


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
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
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

