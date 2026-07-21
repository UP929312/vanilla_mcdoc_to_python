# Generated from symbols.json for ::java::data::advancement::trigger::RequiredConditions
from dataclasses import dataclass
from typing import Generic, TypeVar


C = TypeVar('C')

@dataclass(kw_only=True)
class RequiredConditions(Generic[C]):
    conditions: C


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::RequiredConditions": {
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

