"""
Generated from symbols.json for ::java::util::Filterable
Local link to file: vanilla_mcdoc/util/Filterable.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class Filterable(GeneratedModel, Generic[T]):
    raw: T
    filtered: T | None = None  # Shown only to players with chat filtering enabled.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::Filterable": {
        "kind": "template",
        "child": {
            "kind": "union",
            "members": [
                {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "raw",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::T"
                            }
                        },
                        {
                            "kind": "pair",
                            "desc": "Shown only to players with chat filtering enabled.",
                            "key": "filtered",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::T"
                            },
                            "optional": True
                        }
                    ]
                },
                {
                    "kind": "reference",
                    "path": "::java::util::T"
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::util::T"
            }
        ]
    }
}
