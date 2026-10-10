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
