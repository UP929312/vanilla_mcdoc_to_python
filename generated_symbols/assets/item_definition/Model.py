# Generated from symbols.json for ::java::assets::item_definition::Model
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ModelTint import ModelTint
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class Model:
    model: ModelRef
    tints: list[ModelTint] | None = None
    transformation: Transformation | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Model": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelRef"
                }
            },
            {
                "kind": "pair",
                "key": "tints",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::ModelTint"
                    }
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

