"""
Generated from symbols.json for ::java::assets::font::BitmapProvider
Local link to file: vanilla_mcdoc/assets/font/BitmapProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class BitmapProvider(GeneratedModel):
    file: str
    height: int | None = None
    ascent: int
    chars: Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::BitmapProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "file",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "ascent",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "chars",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "lengthRange": {
                            "kind": 0,
                            "min": 1
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}
