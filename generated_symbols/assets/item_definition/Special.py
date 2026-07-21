# Generated from symbols.json for ::java::assets::item_definition::Special
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class Special:
    model: Any  # Renders a special hardcoded model.
    base: ModelRef  # Base model, providing transformations, particle texture and GUI light.
    transformation: Transformation | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Special": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Renders a special hardcoded model.",
                "key": "model",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "type",
                            "type": {
                                "kind": "reference",
                                "path": "::java::assets::item_definition::SpecialModelType",
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
                                            "type"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:special_item_model"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Base model, providing transformations, particle texture and GUI light.",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelRef"
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

