"""
Generated from symbols.json for ::java::data::util::IntLimiter
Local link to file: generated_symbols/data/util/IntLimiter.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class IntLimiter(GeneratedModel):
    min: int | None = None
    max: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::IntLimiter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
