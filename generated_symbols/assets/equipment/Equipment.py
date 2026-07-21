# Generated from symbols.json for ::java::assets::equipment::Equipment
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef
    from generated_symbols.assets.equipment.Layers import Layers


@dataclass(kw_only=True)
class Equipment:
    layers: Layers  # List of layers for each model layer type.
    trim_palette_replacements: dict[PaletteRef, PaletteRef] | None = None  # Replaces palette textures provided by trim materials.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::Equipment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of layers for each model layer type.",
                "key": "layers",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::equipment::Layers"
                }
            },
            {
                "kind": "pair",
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
                ],
                "desc": "Replaces palette textures provided by trim materials.",
                "key": "trim_palette_replacements",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "reference",
                                "path": "::java::assets::atlas::PaletteRef"
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::assets::atlas::PaletteRef"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

