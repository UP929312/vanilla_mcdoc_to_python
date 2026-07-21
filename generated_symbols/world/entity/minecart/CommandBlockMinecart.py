# Generated from symbols.json for ::java::world::entity::minecart::CommandBlockMinecart
from dataclasses import dataclass
from generated_symbols.world.block.command_block.BaseCommandBlock import BaseCommandBlock
from generated_symbols.world.entity.minecart.Minecart import Minecart


@dataclass(kw_only=True)
class CommandBlockMinecart(Minecart, BaseCommandBlock):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::CommandBlockMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::minecart::Minecart"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::command_block::BaseCommandBlock"
                }
            }
        ]
    }
}

