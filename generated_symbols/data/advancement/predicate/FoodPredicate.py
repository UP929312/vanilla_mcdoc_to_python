# Generated from symbols.json for ::java::data::advancement::predicate::FoodPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class FoodPredicate:
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::FoodPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "level",
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
            },
            {
                "kind": "pair",
                "key": "saturation",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "double"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

