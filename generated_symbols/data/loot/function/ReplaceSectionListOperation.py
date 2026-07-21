# Generated from symbols.json for ::java::data::loot::function::ReplaceSectionListOperation
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ReplaceSectionListOperation:
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ReplaceSectionListOperation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The offset of the section to replace. Defaults to 0.",
                "key": "offset",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The size of the section to replace. Defaults to size of the new list.",
                "key": "size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

