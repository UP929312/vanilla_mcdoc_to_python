"""
Generated from symbols.json for ::java::assets::font::TtfProvider
Local link to file: generated_symbols/assets/font/TtfProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class TtfProvider:
    file: str
    size: float | None = None
    oversample: float | None = None
    shift: tuple[float, float] | None = None
    skip: str | list[str] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::TtfProvider": {
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
                "key": "size",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "oversample",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "shift",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 2,
                        "max": 2
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "skip",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string"
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

