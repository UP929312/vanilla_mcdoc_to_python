# Generated from symbols.json for ::java::util::NonEmptyFlatWeightedList
from typing import TYPE_CHECKING, Annotated, TypeVar

if TYPE_CHECKING:
    from generated_symbols.util.FlatWeightedEntry import FlatWeightedEntry


T = TypeVar('T')

type NonEmptyFlatWeightedList[T] = Annotated[list[FlatWeightedEntry[T]], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::NonEmptyFlatWeightedList": {
        "kind": "template",
        "child": {
            "kind": "list",
            "item": {
                "kind": "concrete",
                "child": {
                    "kind": "reference",
                    "path": "::java::util::FlatWeightedEntry"
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

