# Generated from symbols.json for ::java::util::FlatWeightedList
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from generated_symbols.util.FlatWeightedEntry import FlatWeightedEntry


T = TypeVar('T')

type FlatWeightedList[T] = list[FlatWeightedEntry[T]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::FlatWeightedList": {
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
            }
        },
        "typeParams": [
            {
                "path": "::java::util::T"
            }
        ]
    }
}

