"""
Generated from symbols.json for ::java::assets::shader::post::TextureInput
Local link to file: generated_symbols/assets/shader/post/TextureInput.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class TextureInput:
    location: Annotated[str, IdSpec(registry='texture', path='effect/')]
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
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "texture"
                                        }
                                    },
                                    "path": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "effect/"
                                        }
                                    }
                                }
                            }
                        }
                    ]
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

