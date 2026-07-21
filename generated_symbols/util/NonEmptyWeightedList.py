# Generated from symbols.json for ::java::util::NonEmptyWeightedList
from typing import TYPE_CHECKING, Annotated, TypeVar

if TYPE_CHECKING:
    from generated_symbols.util.WeightedEntry import WeightedEntry


T = TypeVar('T')

type NonEmptyWeightedList[T] = Annotated[list[WeightedEntry[T]], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::NonEmptyWeightedList": {
        "kind": "template",
        "child": {
            "kind": "list",
            "item": {
                "kind": "concrete",
                "child": {
                    "kind": "reference",
                    "path": "::java::util::WeightedEntry"
                },
                "typeArgs": [
                    {
                        "kind": "reference",
                        "path": "::java::util::T"
                    }
                ]
            },
            "lengthRange": {
                "kind": 0,
                "min": 1
            }
        },
        "typeParams": [
            {
                "path": "::java::util::T"
            }
        ]
    }
}

