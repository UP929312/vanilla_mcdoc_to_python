# Generated from symbols.json for ::java::world::component::item::Tool
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.ToolRule import ToolRule


@dataclass(kw_only=True)
class Tool:
    rules: list[ToolRule]  # Blocks that this tool has a special behavior with.
    default_mining_speed: float | None = None  # Used if no rules override it. Defaults to 1.0.
    damage_per_block: int | None = None  # Amount of durability to remove each time a block is broken with this tool. Must be a non-negative integer.
    can_destroy_blocks_in_creative: bool | None = None  # If `false`, players cannot break blocks while holding this tool in creative mode. Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Tool": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Blocks that this tool has a special behavior with.",
                "key": "rules",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::component::item::ToolRule"
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Used if no rules override it. Defaults to 1.0.",
                "key": "default_mining_speed",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Amount of durability to remove each time a block is broken with this tool. Must be a non-negative integer.",
                "key": "damage_per_block",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "If `False`, players cannot break blocks while holding this tool in creative mode. Defaults to `True`.",
                "key": "can_destroy_blocks_in_creative",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

