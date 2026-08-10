"""
Generated from symbols.json for ::java::data::advancement::trigger::InventoryChanged
Local link to file: generated_symbols/data/advancement/trigger/InventoryChanged.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class SlotsStruct:
    empty: MinMaxBounds[int] | int | None = None  # Amount of empty slots.
    occupied: MinMaxBounds[int] | int | None = None  # Amount of occupied slots.
    full: MinMaxBounds[int] | int | None = None  # Amount of slots that are a full stack.


@dataclass(kw_only=True)
class InventoryChanged(TriggerBase):
    slots: SlotsStruct | None = None
    items: list[ItemPredicate] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::InventoryChanged": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
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
}

