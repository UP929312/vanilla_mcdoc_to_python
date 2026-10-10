"""
Generated from symbols.json for ::java::data::worldgen::feature::SingleBlockPillarConfig
Local link to file: generated_symbols/data/worldgen/feature/SingleBlockPillarConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from generated_symbols.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from generated_symbols.util.direction.VerticalDirection import VerticalDirection


class SingleBlockPillarConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: BlockStateProviderRef
    can_replace: BlockPredicate | None = None  # Defaults to "always true".
    direction: VerticalDirection
    chance_to_continue: Annotated[float, Field(ge=0, le=1)] | None = None  # Defaults to 1.
    cap_feature: PlacedFeatureRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SingleBlockPillarConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProviderRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to \"always True\".",
                "key": "can_replace",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "direction",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::VerticalDirection"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to 1.",
                "key": "chance_to_continue",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "cap_feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::placement::PlacedFeatureRef"
                },
                "optional": True
            }
        ]
    }
}

