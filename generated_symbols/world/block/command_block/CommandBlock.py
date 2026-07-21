# Generated from symbols.json for ::java::world::block::command_block::CommandBlock
from dataclasses import dataclass
from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Nameable import Nameable
from generated_symbols.world.block.command_block.BaseCommandBlock import BaseCommandBlock


@dataclass(kw_only=True)
class CommandBlock(BlockEntity, Nameable, BaseCommandBlock):
    powered: bool | None = None  # Whether it is powered by redstone.
    auto: bool | None = None  # Whether it is automatically powered.
    conditionMet: bool | None = None  # Whether the previous command block was successful when the command block was executed. This is always true for non-conditional command blocks.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::command_block::CommandBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Nameable"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::command_block::BaseCommandBlock"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it is powered by redstone.",
                "key": "powered",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether it is automatically powered.",
                "key": "auto",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the previous command block was successful when the command block was executed.\nThis is always True for non-conditional command blocks.",
                "key": "conditionMet",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

