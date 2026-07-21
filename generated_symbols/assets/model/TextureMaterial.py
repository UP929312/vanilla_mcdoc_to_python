# Generated from symbols.json for ::java::assets::model::TextureMaterial
from dataclasses import dataclass


@dataclass(kw_only=True)
class TextureMaterial:
    sprite: str
    force_translucent: bool | None = None  # Whether the texture should be forced into the translucent render pass.  Textures without any translucent pixels are not assigned to the translucent pass by default.  Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::TextureMaterial": {
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
                "desc": "Whether the texture should be forced into the translucent render pass. \\\nTextures without any translucent pixels are not assigned to the translucent pass by default. \\\nDefaults to `False`.",
                "key": "force_translucent",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

