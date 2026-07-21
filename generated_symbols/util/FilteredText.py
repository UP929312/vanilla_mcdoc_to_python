# Generated from symbols.json for ::java::util::FilteredText
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class FilteredText(Generic[T]):
    raw: T
    filtered: T | None = None  # Shown only to players with chat filtering enabled.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::FilteredText": {
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
    }
}

