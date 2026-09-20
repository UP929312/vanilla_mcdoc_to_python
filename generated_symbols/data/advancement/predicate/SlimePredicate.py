"""
Generated from symbols.json for ::java::data::advancement::predicate::SlimePredicate
Local link to file: generated_symbols/data/advancement/predicate/SlimePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


class SlimePredicate(GeneratedModel):
    size: MinMaxBounds[int] | int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::SlimePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "size",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

