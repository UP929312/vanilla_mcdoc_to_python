# Generated from symbols.json for ::java::data::advancement::trigger::InventoryChanged
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate


@dataclass(kw_only=True)
class InventoryChanged(TriggerBase):
    slots: Any | None = None
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

