# Generated from symbols.json for ::java::assets::atlas::PermutationsMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteTexture import PaletteTexture


type PermutationsMap = dict[str, PaletteTexture]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::PermutationsMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "permutation",
                            "value": {
                                "kind": "tree",
                                "values": {
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
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::atlas::PaletteTexture"
                }
            }
        ]
    }
}

