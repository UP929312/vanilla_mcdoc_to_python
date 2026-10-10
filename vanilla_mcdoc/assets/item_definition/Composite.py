"""
Generated from symbols.json for ::java::assets::item_definition::Composite
Local link to file: vanilla_mcdoc/assets/item_definition/Composite.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ItemModel import ItemModel
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


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
