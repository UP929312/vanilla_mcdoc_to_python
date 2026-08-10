"""
Generated from symbols.json for ::java::assets::model::MultipleAxesModelElementRotation
Local link to file: generated_symbols/assets/model/MultipleAxesModelElementRotation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.direction.Axis import Axis


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
                    "path": "::java::util::direction::Axis"
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

