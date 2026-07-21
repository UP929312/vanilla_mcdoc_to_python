# Generated from symbols.json for ::java::world::block::vault::Config
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class Config:
    key_item: ItemStack | None = None  # Item required to open the vault.
    loot_table: str | None = None  # Defaults to "minecraft:chests/trial_chambers/reward".
    override_loot_table_to_display: str | None = None  # The loot table to display items in the vault. Defaults to use the value in `loot_table` field.
    activation_range: float | None = None  # The range when the vault should activate.
    deactivation_range: float | None = None  # The range when the vault should deactivate.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::vault::Config": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Item required to open the vault.",
                "key": "key_item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to \"minecraft:chests/trial_chambers/reward\".",
                "key": "loot_table",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_table"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The loot table to display items in the vault.\nDefaults to use the value in `loot_table` field.",
                "key": "override_loot_table_to_display",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_table"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The range when the vault should activate.",
                "key": "activation_range",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The range when the vault should deactivate.",
                "key": "deactivation_range",
                "type": {
                    "kind": "double"
                },
                "optional": True
            }
        ]
    }
}

