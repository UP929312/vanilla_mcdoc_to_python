# Generated from symbols.json for ::java::data::advancement::predicate::MovementPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class MovementPredicate:
    x: MinMaxBounds[float] | float | None = None
    y: MinMaxBounds[float] | float | None = None
    z: MinMaxBounds[float] | float | None = None
    speed: MinMaxBounds[float] | float | None = None
    horizontal_speed: MinMaxBounds[float] | float | None = None
    vertical_speed: MinMaxBounds[float] | float | None = None
    fall_distance: MinMaxBounds[float] | float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::MovementPredicate": {
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
            },
            {
                "kind": "pair",
                "key": "speed",
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
                "key": "horizontal_speed",
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
                "key": "vertical_speed",
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
                "key": "fall_distance",
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

