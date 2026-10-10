"""
Generated from symbols.json for ::java::assets::atlas::PaletteRef
Local link to file: vanilla_mcdoc/assets/atlas/PaletteRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PaletteRef = Annotated[str, IdSpec(registry='texture', path='palettes/')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::PaletteRef": {
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
                                "value": "palettes/"
                            }
                        }
                    }
                }
            }
        ]
    }
}
