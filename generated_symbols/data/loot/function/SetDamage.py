# Generated from symbols.json for ::java::data::loot::function::SetDamage
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class SetDamage(Conditions):
    damage: NumberProviderRef  # Decimal percentage. Can be negative when used in combination with `add`.  Clamps to a float between `-1` & `1` (inclusive).
    add: bool | None = None  # Whether to add to the existing damage of the item. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetDamage": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Decimal percentage. Can be negative when used in combination with `add`. \\\nClamps to a float between `-1` & `1` (inclusive).",
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
                            "path": "::java::data::number_provider::NumberProviderRef",
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

