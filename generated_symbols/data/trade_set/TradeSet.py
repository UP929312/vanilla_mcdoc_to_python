"""
Generated from symbols.json for ::java::data::trade_set::TradeSet
Local link to file: generated_symbols/data/trade_set/TradeSet.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.IntNumberProvider import IntNumberProvider


class TradeSet(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'trade_set'

    trades: Annotated[str, IdSpec(registry='villager_trade', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_trade')]]  # Possible trade generators.
    amount: IntNumberProvider  # Amount of trades to be generated.
    allow_duplicates: bool | None = None  # Whether the trade set can use the same generator multiple times and generate duplicate trades. Defaults to `false`.
    random_sequence: Annotated[str, IdSpec(registry='random_sequence', definition=True)] | None = None


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
                "desc": "Amount of trades to be generated.",
                "key": "amount",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::IntNumberProvider"
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

