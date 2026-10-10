"""
Generated from symbols.json for ::java::util::FlatWeightedList
Local link to file: vanilla_mcdoc/util/FlatWeightedList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from vanilla_mcdoc.util.FlatWeightedEntry import FlatWeightedEntry


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
