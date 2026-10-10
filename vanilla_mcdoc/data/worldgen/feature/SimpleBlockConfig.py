"""
Generated from symbols.json for ::java::data::worldgen::feature::SimpleBlockConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/SimpleBlockConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef import BlockStateProviderRef


class SimpleBlockConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    to_place: BlockStateProviderRef
    schedule_tick: bool | None = None  # Whether to schedule a block update. Defaults to `false`.
