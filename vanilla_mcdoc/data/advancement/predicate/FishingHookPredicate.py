"""
Generated from symbols.json for ::java::data::advancement::predicate::FishingHookPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/FishingHookPredicate.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class FishingHookPredicate(GeneratedModel):
    in_open_water: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::FishingHookPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "in_open_water",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
