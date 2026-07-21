# Generated from symbols.json for ::java::data::advancement::predicate::SlimePredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class SlimePredicate:
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

