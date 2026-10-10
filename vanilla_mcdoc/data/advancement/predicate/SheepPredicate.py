"""
Generated from symbols.json for ::java::data::advancement::predicate::SheepPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/SheepPredicate.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class SheepPredicate(GeneratedModel):
    sheared: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::SheepPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sheared",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::DyeColor"
                },
                "optional": True
            }
        ]
    }
}
