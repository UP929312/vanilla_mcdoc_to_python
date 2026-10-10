"""
Generated from symbols.json for ::java::world::block::command_block::CommandBlock
Local link to file: vanilla_mcdoc/world/block/command_block/CommandBlock.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Nameable import Nameable
from vanilla_mcdoc.world.block.command_block.BaseCommandBlock import BaseCommandBlock


class CommandBlock(BaseCommandBlock, BlockEntity, Nameable):
    powered: bool | None = None  # Whether it is powered by redstone.
    auto: bool | None = None  # Whether it is automatically powered.
    conditionMet: bool | None = None  # Whether the previous command block was successful when the command block was executed. This is always true for non-conditional command blocks.
