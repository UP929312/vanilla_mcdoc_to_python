"""
Generated from symbols.json for ::java::data::slot_source::SlotSource
Local link to file: generated_symbols/data/slot_source/SlotSource.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.slot_source.TypedSlotSource import TypedSlotSource
    from generated_symbols.registry.KnownSlotSourceId import KnownSlotSourceId


type SlotSource = TypedSlotSource | list[SlotSource] | Annotated[str, IdSpec(registry='slot_source', tags='allowed')] | KnownSlotSourceId


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

