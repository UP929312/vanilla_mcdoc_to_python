"""
Generated from symbols.json for ::java::data::advancement::trigger::ParitalRequired
Local link to file: vanilla_mcdoc/data/advancement/trigger/ParitalRequired.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


C = TypeVar('C')


class ParitalRequired(GeneratedModel, Generic[C]):
    conditions: C


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ParitalRequired": {
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
                    }
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
