"""
Generated from symbols.json for ::java::world::block::test_instance_block::TestInstanceBlockData
Local link to file: vanilla_mcdoc/world/block/test_instance_block/TestInstanceBlockData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.registry.KnownTestInstanceId import KnownTestInstanceId
    from vanilla_mcdoc.util.Rotation import Rotation
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlockStatus import TestInstanceBlockStatus


class TestInstanceBlockData(GeneratedModel):
    test: Annotated[str, IdSpec(registry='test_instance')] | KnownTestInstanceId | None = None
    size: tuple[int, int, int]
    rotation: Rotation
    ignore_entities: bool
    status: TestInstanceBlockStatus
    error_message: Text | None = None
