"""
Generated from symbols.json for ::java::data::worldgen::feature::SingleBlockPillarConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SingleBlockPillarConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef import PlacedFeatureRef
    from vanilla_mcdoc.util.direction.VerticalDirection import VerticalDirection


class SingleBlockPillarConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    block: BlockStateProviderRef
    can_replace: BlockPredicate | None = None  # Defaults to "always true".
    direction: VerticalDirection
    chance_to_continue: Annotated[float, Field(ge=0, le=1)] | None = None  # Defaults to 1.
    cap_feature: PlacedFeatureRef | None = None
