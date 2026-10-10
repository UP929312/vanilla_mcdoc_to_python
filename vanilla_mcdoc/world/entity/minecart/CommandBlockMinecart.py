"""
Generated from symbols.json for ::java::world::entity::minecart::CommandBlockMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/CommandBlockMinecart.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.block.command_block.BaseCommandBlock import BaseCommandBlock
from vanilla_mcdoc.world.entity.minecart.Minecart import Minecart


class CommandBlockMinecart(BaseCommandBlock, Minecart):
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
