"""
Generated from symbols.json for ::java::data::block_transformer::BlockTransformData
Local link to file: vanilla_mcdoc/data/block_transformer/BlockTransformData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.block_transformer.BlockTransformDropStrategy import BlockTransformDropStrategy
    from vanilla_mcdoc.data.block_transformer.BlockTransformParticle import BlockTransformParticle
    from vanilla_mcdoc.data.block_transformer.BlockTransformType import BlockTransformType
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef
    from vanilla_mcdoc.util.direction.Direction import Direction


class BlockTransformData(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'block_transformer'

    block_state_provider: BlockStateProviderRef  # If the provider returns no result, the next transformer will be attempted.
    sound: SoundEventRef | None = None  # Defaults to not playing sound.
    particle: BlockTransformParticle | None = None  # Defaults to `none`.
    disallowed_faces: list[Direction] | None = None  # If a disallowed face is interacted with, the next transformer will be attempted.  Defaults to empty (allowing all faces).
    loot: Annotated[str, IdSpec(registry='loot_table')] | None = None  # The loot to drop on a successful transformation.  Defaults to drop nothing.
    drop_strategy: BlockTransformDropStrategy | None = None  # Where the `loot` should drop.  Defaults to `from_middle`.
    transform_type: BlockTransformType | None = None  # How nearby blocks are affected by the transformation.  Defaults to `single_block`.
    update_from_neighbors: bool | None = None  # Whether the transformed block should update based on neighboring blocks.  Defaults to `true`.
    consume_on_use: bool | None = None  # Only has effect on stackable items.  Defaults to `true`.
    item_damage_per_use: Annotated[int, Field(ge=0)] | None = None  # Only has effect on unstackable items.  Defauls to 1.
