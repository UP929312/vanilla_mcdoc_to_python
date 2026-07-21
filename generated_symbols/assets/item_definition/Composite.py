# Generated from symbols.json for ::java::assets::item_definition::Composite
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class Composite:
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

