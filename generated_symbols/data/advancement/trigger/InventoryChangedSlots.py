# Generated from symbols.json for ::java::data::advancement::trigger::InventoryChangedSlots
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class InventoryChangedSlots:
    empty: MinMaxBounds[int] | int | None = None  # Amount of empty slots.
    occupied: MinMaxBounds[int] | int | None = None  # Amount of occupied slots.
    full: MinMaxBounds[int] | int | None = None  # Amount of slots that are a full stack.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::InventoryChangedSlots": {
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
    }
}

