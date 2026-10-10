"""
Generated from symbols.json for ::java::data::loot::function::SetEnchantments
Local link to file: generated_symbols/data/loot/function/SetEnchantments.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class SetEnchantments(Conditions):
    enchantments: dict[Annotated[str, IdSpec(registry='enchantment')], IntNumberProviderRef]  # A map of enchantments to levels. Setting an enchantment to `0` removes it from the item.
    add: bool | None = None  # Whether to add to the level of each enchantment. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetEnchantments": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A map of enchantments to levels. Setting an enchantment to `0` removes it from the item.",
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
                                "path": "::java::data::number_provider::IntNumberProviderRef"
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
