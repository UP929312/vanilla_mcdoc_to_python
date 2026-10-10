"""
Generated from symbols.json for ::java::assets::model::ModelOverride
Local link to file: generated_symbols/assets/model/ModelOverride.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.assets.model.Predicates import Predicates


class ModelOverride(GeneratedModel):
    predicate: dict[Predicates, float]
    model: ModelRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelOverride": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
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
            },
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelRef"
                }
            }
        ]
    }
}
