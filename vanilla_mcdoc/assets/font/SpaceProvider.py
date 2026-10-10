"""
Generated from symbols.json for ::java::assets::font::SpaceProvider
Local link to file: vanilla_mcdoc/assets/font/SpaceProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class SpaceProvider(GeneratedModel):
    advances: dict[Annotated[str, Field(min_length=1, max_length=1)], float]


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
