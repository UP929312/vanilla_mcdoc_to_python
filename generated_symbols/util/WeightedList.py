# Generated from symbols.json for ::java::util::WeightedList
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from generated_symbols.util.WeightedEntry import WeightedEntry


T = TypeVar('T')

type WeightedList[T] = list[WeightedEntry[T]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::WeightedList": {
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
            }
        },
        "typeParams": [
            {
                "path": "::java::util::T"
            }
        ]
    }
}

