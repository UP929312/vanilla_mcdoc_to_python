# Generated from symbols.json for ::java::assets::atlas::PaletteTexture
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef


type PaletteTexture = PaletteRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::PaletteTexture": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
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
            },
            {
                "kind": "reference",
                "path": "::java::assets::atlas::PaletteRef",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

