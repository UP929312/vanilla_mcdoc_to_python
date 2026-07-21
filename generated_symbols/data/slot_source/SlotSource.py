# Generated from symbols.json for ::java::data::slot_source::SlotSource
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.TypedSlotSource import TypedSlotSource


type SlotSource = TypedSlotSource | list[SlotSource] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::SlotSource": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::slot_source::TypedSlotSource"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::slot_source::SlotSource"
                }
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "slot_source"
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
            }
        ]
    }
}

