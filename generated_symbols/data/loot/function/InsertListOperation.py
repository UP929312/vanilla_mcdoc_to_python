# Generated from symbols.json for ::java::data::loot::function::InsertListOperation
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class InsertListOperation:
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::InsertListOperation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The offset in the list to insert into. Defaults to 0.",
                "key": "offset",
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

