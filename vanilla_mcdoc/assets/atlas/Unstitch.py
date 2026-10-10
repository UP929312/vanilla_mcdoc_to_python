"""
Generated from symbols.json for ::java::assets::atlas::Unstitch
Local link to file: vanilla_mcdoc/assets/atlas/Unstitch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.UnstitchRegion import UnstitchRegion


class Unstitch(GeneratedModel):
    resource: Annotated[str, IdSpec(registry='texture')]
    divisor_x: float | None = None  # If set to the resource width, regions will use pixel coordinates.
    divisor_y: float | None = None  # If set to the resource height, regions will use pixel coordinates.
    regions: list[UnstitchRegion]


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
