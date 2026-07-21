# Generated from symbols.json for ::java::world::entity::mob::warden::Suspect
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Suspect:
    anger: Annotated[int, 'Range | `1`-`150` | both inclusive'] | None = None  # Level of anger that will decrease by 1 every second.
    uuid: tuple[int, int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::warden::Suspect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Level of anger that will decrease by 1 every second.",
                "key": "anger",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 150
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "uuid",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

