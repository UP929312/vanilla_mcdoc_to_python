# Generated from symbols.json for ::java::data::util::IntLimiter
from dataclasses import dataclass


@dataclass(kw_only=True)
class IntLimiter:
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

