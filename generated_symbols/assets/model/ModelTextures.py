# Generated from symbols.json for ::java::assets::model::ModelTextures
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.model.TextureMaterial import TextureMaterial


type ModelTextures = dict[str, str | TextureMaterial]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelTextures": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "texture_slot",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "kind": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "definition"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "texture_slot",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "kind": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "value"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::assets::model::TextureMaterial",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.1"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

