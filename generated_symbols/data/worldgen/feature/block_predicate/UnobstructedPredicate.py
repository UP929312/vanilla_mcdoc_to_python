# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::UnobstructedPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class UnobstructedPredicate:
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

