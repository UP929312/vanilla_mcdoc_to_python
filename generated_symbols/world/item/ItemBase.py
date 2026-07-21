# Generated from symbols.json for ::java::world::item::ItemBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Trim import Trim
    from generated_symbols.world.item.AttributeModifier import AttributeModifier
    from generated_symbols.world.item.Display import Display
    from generated_symbols.world.item.Enchantment import Enchantment


@dataclass(kw_only=True)
class ItemBase:
    key_name: Any  # Custom item NBT tags
    Damage: int | None = None  # Damage that an item has. Only used for tools, armor, etc.
    Unbreakable: bool | None = None  # Whether the item should be unbreakable. Only used for tools, armor, etc.
    CanDestroy: list[str] | None = None  # List of the block states that can be destroyed by this item when holding it in adventure mode.
    CanPlaceOn: list[str] | None = None  # List of blockstates that this block item can be placed on.
    CustomModelData: int | None = None  # Tag that describes the custom model an item will take. Used by the `custom_model_data` model overrides predicate. Has certain restrictions due to float conversion.
    Enchantments: list[Enchantment] | None = None  # List of enchantments that are on the item.
    RepairCost: int | None = None  # Number of experience levels to add to the base level cost when repairing, combining, or renaming this item with an anvil.
    AttributeModifiers: list[AttributeModifier] | None = None  # Applied to an entity that has equipped the item.
    display: Display | None = None  # Display settings.
    HideFlags: int | None = None  # Bitfield for which flags to hide on an item.
    Trim: Trim | None = None  # Trim to apply to the item & armor when worn.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::ItemBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Damage that an item has. Only used for tools, armor, etc.",
                "key": "Damage",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the item should be unbreakable.\nOnly used for tools, armor, etc.",
                "key": "Unbreakable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of the block states that can be destroyed by this item when holding it in adventure mode.",
                "key": "CanDestroy",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "block_predicate"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of blockstates that this block item can be placed on.",
                "key": "CanPlaceOn",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "block_predicate"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Tag that describes the custom model an item will take.\nUsed by the `custom_model_data` model overrides predicate.\nHas certain restrictions due to float conversion.",
                "key": "CustomModelData",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of enchantments that are on the item.",
                "key": "Enchantments",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::Enchantment"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of experience levels to add to the base level cost when repairing, combining, or renaming this item with an anvil.",
                "key": "RepairCost",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Applied to an entity that has equipped the item.",
                "key": "AttributeModifiers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::item::AttributeModifier"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Display settings.",
                "key": "display",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::Display"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "bitfield",
                        "value": {
                            "kind": "reference",
                            "path": "::java::world::item::HideFlags"
                        }
                    }
                ],
                "desc": "Bitfield for which flags to hide on an item.",
                "key": "HideFlags",
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
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "desc": "Trim to apply to the item & armor when worn.",
                "key": "Trim",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::Trim"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Custom item NBT tags",
                "key": {
                    "kind": "string"
                },
                "type": {
                    "kind": "any"
                }
            }
        ]
    }
}

