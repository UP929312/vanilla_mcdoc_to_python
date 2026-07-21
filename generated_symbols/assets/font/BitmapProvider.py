# Generated from symbols.json for ::java::assets::font::BitmapProvider
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class BitmapProvider:
    file: str
    ascent: int
    chars: Annotated[list[Annotated[str, 'Length = 1 (inclusive) and above']], 'Length = 1 (inclusive) and above']
    height: int | None = None


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

