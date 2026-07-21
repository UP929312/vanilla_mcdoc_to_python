# Generated from symbols.json for ::java::util::FlatWeightedEntry
from dataclasses import dataclass
from typing import Annotated, Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class FlatWeightedEntry(Generic[T]):
    weight: Annotated[int, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::FlatWeightedEntry": {
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
                    "kind": "spread",
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

