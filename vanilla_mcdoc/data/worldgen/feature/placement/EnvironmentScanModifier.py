"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::EnvironmentScanModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/EnvironmentScanModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from vanilla_mcdoc.util.direction.VerticalDirection import VerticalDirection


class EnvironmentScanModifier(GeneratedModel):
    direction_of_search: VerticalDirection
    max_steps: Annotated[int, Field(ge=1, le=32)]
    target_condition: BlockPredicate
    allowed_search_condition: BlockPredicate | None = None
