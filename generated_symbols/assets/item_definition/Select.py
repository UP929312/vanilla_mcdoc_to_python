# Generated from symbols.json for ::java::assets::item_definition::Select
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.assets.item_definition.SelectPropertyType import SelectPropertyType
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class Select:
    property: SelectPropertyType
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Select": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "property",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::SelectPropertyType",
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
                    "registry": "minecraft:select_item_property"
                }
            },
            {
                "kind": "pair",
                "desc": "Item model to render if none of the cases matched the value.",
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

