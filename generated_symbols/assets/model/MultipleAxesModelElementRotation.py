# Generated from symbols.json for ::java::assets::model::MultipleAxesModelElementRotation
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.model.Axis import Axis


type MultipleAxesModelElementRotation = dict[Axis, float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::MultipleAxesModelElementRotation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelElementRotationBase"
                }
            },
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::assets::model::Axis"
                },
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.21.11"
                    }
                }
            }
        ]
    }
}

