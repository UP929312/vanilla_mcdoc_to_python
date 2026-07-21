# Generated from symbols.json for ::java::assets::shader::post::TextureInput
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TextureInput:
    location: str
    sampler_name: str
    width: Annotated[int, 'Range | Min `1` and above | inclusive']
    height: Annotated[int, 'Range | Min `1` and above | inclusive']
    bilinear: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::TextureInput": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "location",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "sampler_name",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "bilinear",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

