"""
Generated from symbols.json for ::java::assets::model::ModelOverridePredicates
Local link to file: generated_symbols/assets/model/ModelOverridePredicates.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.model.Predicates import Predicates


type ModelOverridePredicates = dict[Predicates, float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelOverridePredicates": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::assets::model::Predicates"
                },
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

