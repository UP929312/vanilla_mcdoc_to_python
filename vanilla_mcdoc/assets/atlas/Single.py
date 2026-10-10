"""
Generated from symbols.json for ::java::assets::atlas::Single
Local link to file: vanilla_mcdoc/assets/atlas/Single.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Single(GeneratedModel):
    resource: Annotated[str, IdSpec(registry='texture')]  # A single texture location of the source.
    sprite: Annotated[str, IdSpec(registry='texture', definition=True)] | None = None  # The identifier of the sprite that can referenced. If not specified, matches `resource`.


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
