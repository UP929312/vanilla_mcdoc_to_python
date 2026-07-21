# Generated from symbols.json for ::java::data::advancement::predicate::FishingHookPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class FishingHookPredicate:
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

