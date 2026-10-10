"""
Generated from symbols.json for ::java::data::advancement::trigger::BlockStateConditions
Local link to file: vanilla_mcdoc/data/advancement/trigger/BlockStateConditions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.registry_ref.BlockListRef import BlockListRef


class BlockStateConditions(GeneratedModel):
    blocks: BlockListRef | None = None
    state: dict[str, str] | None = None
