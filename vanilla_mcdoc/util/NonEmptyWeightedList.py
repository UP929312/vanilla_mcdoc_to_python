"""
Generated from symbols.json for ::java::util::NonEmptyWeightedList
Local link to file: vanilla_mcdoc/util/NonEmptyWeightedList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, TypeVar

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.util.WeightedEntry import WeightedEntry


T = TypeVar('T')


type NonEmptyWeightedList[T] = Annotated[list[WeightedEntry[T]], Field(min_length=1)]


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
