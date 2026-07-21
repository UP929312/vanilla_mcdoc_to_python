# Generated from symbols.json for ::java::assets::model::ModelOverride
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.assets.model.Predicates import Predicates


@dataclass(kw_only=True)
class ModelOverride:
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

