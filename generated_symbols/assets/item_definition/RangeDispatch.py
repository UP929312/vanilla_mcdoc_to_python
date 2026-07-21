# Generated from symbols.json for ::java::assets::item_definition::RangeDispatch
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.NumericPropertyType import NumericPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class RangeDispatch:
    property: NumericPropertyType
    entries: list[Any]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::RangeDispatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::NumericPropertyType",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "property"
                            ]
                        }
                    ],
                    "registry": "minecraft:numeric_item_property"
                }
            },
            {
                "kind": "pair",
                "desc": "Factor to multiply the property value with. Defaults to 1.",
                "key": "scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of ranges. Will select last entry with threshold less or equal to value.\nOrder does not matter, list will be sorted by threshold in ascending order.",
                "key": "entries",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "threshold",
                                "type": {
                                    "kind": "float"
                                }
                            },
                            {
                                "kind": "pair",
                                "key": "model",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::item_definition::ItemModel"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Item model to render if no entries were less or equal to the value.",
                "key": "fallback",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                },
                "optional": True
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "transformation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Transformation"
                },
                "optional": True
            }
        ]
    }
}

