# Generated from symbols.json for ::java::data::loot::function::SetEnchantments
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class SetEnchantments(Conditions):
    enchantments: dict[str, NumberProviderRef]  # A map of enchantments to levels. Setting an enchantment to `0` removes it from the item.  Each level is clamped to a positive integer.
    add: bool | None = None  # Whether to add to the level of each enchantment. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetEnchantments": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A map of enchantments to levels. Setting an enchantment to `0` removes it from the item. \\\nEach level is clamped to a positive integer.",
                "key": "enchantments",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "enchantment"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::number_provider::NumberProviderRef"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Whether to add to the level of each enchantment. Defaults to `False`.",
                "key": "add",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

