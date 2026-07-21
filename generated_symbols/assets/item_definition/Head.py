# Generated from symbols.json for ::java::assets::item_definition::Head
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.HeadType import HeadType


@dataclass(kw_only=True)
class Head:
    kind: HeadType
    texture: str | None = None  # Texture to use instead of the texture from `kind`.
    animation: float | None = None  # Controls the animation time for piglin and dragon heads. Defaults to `0`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Head": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "kind",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::HeadType"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Texture to use instead of the texture from `kind`.\nIf present, will ignore the `profile` component.",
                            "key": "texture",
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
                                                        "value": "entity/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Texture to use instead of the texture from `kind`.",
                            "key": "texture",
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
                                                        "value": "entity/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Controls the animation time for piglin and dragon heads. Defaults to `0`.",
                "key": "animation",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

