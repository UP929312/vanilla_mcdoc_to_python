"""
Generated from symbols.json for ::java::util::text::SpriteText
Local link to file: vanilla_mcdoc/util/text/SpriteText.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.util.text.ObjectTextConfig import ObjectTextConfig
from vanilla_mcdoc.util.text.TextBase import TextBase


class SpriteText(ObjectTextConfig, TextBase):
    atlas: Annotated[str, IdSpec(registry='atlas')] | None = None  # Defaults to `minecraft:blocks`.
    sprite: Annotated[str, IdSpec(registry='texture')]
    object: Literal['atlas'] | None = 'atlas'
    type: Literal['object'] | None = 'object'


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::SpriteText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to `minecraft:blocks`.",
                "key": "atlas",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "atlas"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sprite",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ObjectTextConfig"
                }
            },
            {
                "kind": "pair",
                "key": "object",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "atlas"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "object"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextBase"
                }
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.21.9"
                    }
                }
            }
        ]
    }
}
