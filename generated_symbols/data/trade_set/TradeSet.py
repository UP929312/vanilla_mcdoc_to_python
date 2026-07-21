# Generated from symbols.json for ::java::data::trade_set::TradeSet
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProvider import NumberProvider


@dataclass(kw_only=True)
class TradeSet:
    trades: str | list[str]  # Possible trade generators.
    amount: NumberProvider  # Amount of trades to be generated.  Clamps to an integer of at least `1`.
    allow_duplicates: bool | None = None  # Whether the trade set can use the same generator multiple times and generate duplicate trades. Defaults to `false`.
    random_sequence: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::trade_set::TradeSet": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Possible trade generators.",
                "key": "trades",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "villager_trade"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "villager_trade"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Amount of trades to be generated. \\\nClamps to an integer of at least `1`.",
                "key": "amount",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProvider"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the trade set can use the same generator multiple times and generate duplicate trades.\nDefaults to `False`.",
                "key": "allow_duplicates",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "random_sequence",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "random_sequence"
                                        }
                                    },
                                    "definition": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "boolean",
                                            "value": True
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

