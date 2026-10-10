"""
Generated from symbols.json for ::java::assets::atlas::PaletteTexture
Local link to file: vanilla_mcdoc/assets/atlas/PaletteTexture.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.assets.atlas.PaletteRef import PaletteRef


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
