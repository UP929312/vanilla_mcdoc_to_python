"""
Generated from symbols.json for ::java::data::advancement::trigger::InventoryChangeTrigger
Local link to file: generated_symbols/data/advancement/trigger/InventoryChangeTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class SlotsStruct:
    empty: MinMaxBounds[int] | int | None = None  # Amount of empty slots.
    occupied: MinMaxBounds[int] | int | None = None  # Amount of occupied slots.
    full: MinMaxBounds[int] | int | None = None  # Amount of slots that are a full stack.


@dataclass(kw_only=True)
class InventoryChangeTriggerTypeArg(PlayerConditions):
    slots: SlotsStruct | None = None
    items: list[ItemPredicate] | None = None


InventoryChangeTrigger = AllOptional[InventoryChangeTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::InventoryChangeTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::PlayerConditions"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "slots",
                        "type": {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "desc": "Amount of empty slots.",
                                    "key": "empty",
                                    "type": {
                                        "kind": "concrete",
                                        "child": {
                                            "kind": "reference",
                                            "path": "::java::data::util::MinMaxBounds"
                                        },
                                        "typeArgs": [
                                            {
                                                "kind": "int"
                                            }
                                        ]
                                    },
                                    "optional": True
                                },
                                {
                                    "kind": "pair",
                                    "desc": "Amount of occupied slots.",
                                    "key": "occupied",
                                    "type": {
                                        "kind": "concrete",
                                        "child": {
                                            "kind": "reference",
                                            "path": "::java::data::util::MinMaxBounds"
                                        },
                                        "typeArgs": [
                                            {
                                                "kind": "int"
                                            }
                                        ]
                                    },
                                    "optional": True
                                },
                                {
                                    "kind": "pair",
                                    "desc": "Amount of slots that are a full stack.",
                                    "key": "full",
                                    "type": {
                                        "kind": "concrete",
                                        "child": {
                                            "kind": "reference",
                                            "path": "::java::data::util::MinMaxBounds"
                                        },
                                        "typeArgs": [
                                            {
                                                "kind": "int"
                                            }
                                        ]
                                    },
                                    "optional": True
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "items",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::advancement::predicate::ItemPredicate"
                            }
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

