# Generated from symbols.json for ::java::util::text::SpriteText
from dataclasses import dataclass
from generated_symbols.util.text.ObjectTextConfig import ObjectTextConfig
from generated_symbols.util.text.TextBase import TextBase


@dataclass(kw_only=True)
class SpriteText(ObjectTextConfig, TextBase):
    sprite: str
    atlas: str | None = None  # Defaults to `minecraft:blocks`.
    object: str | None = None
    type: str | None = None


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

