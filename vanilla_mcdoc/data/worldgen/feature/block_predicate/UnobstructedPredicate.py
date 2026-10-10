"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::UnobstructedPredicate
Local link to file: vanilla_mcdoc/data/worldgen/feature/block_predicate/UnobstructedPredicate.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class UnobstructedPredicate(GeneratedModel):
    offset: tuple[int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::UnobstructedPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}
