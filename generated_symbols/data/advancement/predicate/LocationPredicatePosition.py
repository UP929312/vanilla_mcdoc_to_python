# Generated from symbols.json for ::java::data::advancement::predicate::LocationPredicatePosition
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class LocationPredicatePosition:
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LocationPredicatePosition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "x",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "y",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "z",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

