"""
Generated from symbols.json for ::java::data::advancement::trigger::AllOptional
Local link to file: generated_symbols/data/advancement/trigger/AllOptional.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


C = TypeVar('C')

class AllOptional(GeneratedModel, Generic[C]):
    conditions: C | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::AllOptional": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "conditions",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::advancement::trigger::C"
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::advancement::trigger::C"
            }
        ]
    }
}

