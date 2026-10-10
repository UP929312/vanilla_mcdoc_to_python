"""
Generated from symbols.json for ::java::data::loot::function::SetDamage
Local link to file: vanilla_mcdoc/data/loot/function/SetDamage.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class SetDamage(Conditions):
    damage: FloatNumberProviderRef  # Decimal percentage. Can be negative when used in combination with `add`.  Accepts a value between `-1` & `1` (inclusive).
    add: bool | None = None  # Whether to add to the existing damage of the item. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetDamage": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Decimal percentage. Can be negative when used in combination with `add`. \\\nAccepts a value between `-1` & `1` (inclusive).",
                "key": "damage",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::RandomValueBounds",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::number_provider::FloatNumberProviderRef",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Whether to add to the existing damage of the item. Defaults to `False`.",
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
