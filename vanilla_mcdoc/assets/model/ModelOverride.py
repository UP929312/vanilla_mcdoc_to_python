"""
Generated from symbols.json for ::java::assets::model::ModelOverride
Local link to file: vanilla_mcdoc/assets/model/ModelOverride.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.ModelRef import ModelRef
    from vanilla_mcdoc.assets.model.Predicates import Predicates


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
