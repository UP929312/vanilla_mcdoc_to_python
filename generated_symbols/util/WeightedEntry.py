# Generated from symbols.json for ::java::util::WeightedEntry
from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class WeightedEntry(Generic[T]):
    weight: Annotated[int, 'Range | Min `0` and above | inclusive']
    data: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::WeightedEntry": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "weight",
                    "type": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": 0
                        }
                    }
                },
                {
                    "kind": "pair",
                    "key": "data",
                    "type": {
                        "kind": "reference",
                        "path": "::java::util::T"
                    }
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

