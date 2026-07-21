# Generated from symbols.json for ::java::assets::font::SpaceProvider
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class SpaceProvider:
    advances: dict[Annotated[str, 'Length = 1'], float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::SpaceProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "advances",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "lengthRange": {
                                    "kind": 0,
                                    "min": 1,
                                    "max": 1
                                }
                            },
                            "type": {
                                "kind": "float"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

