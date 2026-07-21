# Generated from symbols.json for ::java::data::advancement::predicate::FluidPredicateState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


type FluidPredicateState = dict[str, MinMaxBounds[int] | int | bool | str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::FluidPredicateState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string"
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
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
                        {
                            "kind": "boolean"
                        },
                        {
                            "kind": "string"
                        }
                    ]
                }
            }
        ]
    }
}

