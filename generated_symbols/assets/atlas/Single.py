# Generated from symbols.json for ::java::assets::atlas::Single
from dataclasses import dataclass


@dataclass(kw_only=True)
class Single:
    resource: str  # A single texture location of the source.
    sprite: str | None = None  # The identifier of the sprite that can referenced. If not specified, matches `resource`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::Single": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A single texture location of the source.",
                "key": "resource",
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
                "kind": "pair",
                "desc": "The identifier of the sprite that can referenced.\nIf not specified, matches `resource`.",
                "key": "sprite",
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
                                    "definition": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "boolean",
                                            "value": True
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
}

