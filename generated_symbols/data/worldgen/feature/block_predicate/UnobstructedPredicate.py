"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::UnobstructedPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/UnobstructedPredicate.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


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

