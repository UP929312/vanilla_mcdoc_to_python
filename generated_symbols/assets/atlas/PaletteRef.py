# Generated from symbols.json for ::java::assets::atlas::PaletteRef
from typing import Annotated

from runtime_metadata import IdSpec


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

