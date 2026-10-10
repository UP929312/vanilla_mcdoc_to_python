"""
Generated from symbols.json for ::java::data::advancement::predicate::RaiderPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/RaiderPredicate.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class RaiderPredicate(GeneratedModel):
    has_raid: bool | None = None
    is_captain: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::RaiderPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "has_raid",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_captain",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
