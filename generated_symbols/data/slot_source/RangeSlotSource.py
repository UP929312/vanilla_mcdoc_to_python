# Generated from symbols.json for ::java::data::slot_source::RangeSlotSource
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.BlockEntityTarget import BlockEntityTarget
    from generated_symbols.data.loot.EntityTarget import EntityTarget


@dataclass(kw_only=True)
class RangeSlotSource:
    slots: str
    source: EntityTarget | BlockEntityTarget | str | None = None  # Defaults to `container`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::RangeSlotSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "source",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::loot::EntityTarget"
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::loot::BlockEntityTarget"
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
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
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Defaults to `container`.",
                            "key": "source",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::loot::EntityTarget"
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::loot::BlockEntityTarget"
                                    },
                                    {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "container"
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "slots",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "item_slots"
                        }
                    ]
                }
            }
        ]
    }
}

