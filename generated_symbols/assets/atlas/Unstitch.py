# Generated from symbols.json for ::java::assets::atlas::Unstitch
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.UnstitchRegion import UnstitchRegion


@dataclass(kw_only=True)
class Unstitch:
    resource: str
    regions: list[UnstitchRegion]
    divisor_x: float | None = None  # If set to the resource width, regions will use pixel coordinates.
    divisor_y: float | None = None  # If set to the resource height, regions will use pixel coordinates.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::Unstitch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                "desc": "If set to the resource width, regions will use pixel coordinates.",
                "key": "divisor_x",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If set to the resource height, regions will use pixel coordinates.",
                "key": "divisor_y",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "regions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::atlas::UnstitchRegion"
                    }
                }
            }
        ]
    }
}

