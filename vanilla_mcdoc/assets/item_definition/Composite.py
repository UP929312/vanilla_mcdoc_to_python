"""
Generated from symbols.json for ::java::assets::item_definition::Composite
Local link to file: generated_symbols/assets/item_definition/Composite.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.world.entity.display.Transformation import Transformation


class Composite(GeneratedModel):
    models: list[ItemModel]
    transformation: Transformation | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Composite": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "models",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::ItemModel"
                    }
                }
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
