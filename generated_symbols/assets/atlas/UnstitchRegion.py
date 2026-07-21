# Generated from symbols.json for ::java::assets::atlas::UnstitchRegion
from dataclasses import dataclass


@dataclass(kw_only=True)
class UnstitchRegion:
    sprite: str
    x: float
    y: float
    width: float
    height: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::UnstitchRegion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                }
            },
            {
                "kind": "pair",
                "key": "x",
                "type": {
                    "kind": "double"
                }
            },
            {
                "kind": "pair",
                "key": "y",
                "type": {
                    "kind": "double"
                }
            },
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "double"
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "double"
                }
            }
        ]
    }
}

