"""
Generated from symbols.json for ::java::util::game_event::PositionSource
Local link to file: vanilla_mcdoc/util/game_event/PositionSource.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.util.game_event.BlockPositionSource import BlockPositionSource
from vanilla_mcdoc.util.game_event.EntityPositionSource import EntityPositionSource


class PositionSourceBlock(BlockPositionSource):
    type: Literal['minecraft:block', 'block'] = 'minecraft:block'


class PositionSourceEntity(EntityPositionSource):
    type: Literal['minecraft:entity', 'entity'] = 'minecraft:entity'


type PositionSource = Annotated[
    PositionSourceBlock | PositionSourceEntity,
    Field(discriminator='type'),
]
