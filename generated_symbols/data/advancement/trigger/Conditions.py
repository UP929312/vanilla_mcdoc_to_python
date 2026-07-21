# Generated from symbols.json for ::java::data::advancement::trigger::Conditions
from dataclasses import dataclass
from typing import Generic, TypeVar


C = TypeVar('C')

@dataclass(kw_only=True)
class Conditions(Generic[C]):
    conditions: C | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::Conditions": {
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

