"""
Generated from symbols.json for ::java::data::worldgen::material_condition::StoneDepthCondition
Local link to file: vanilla_mcdoc/data/worldgen/material_condition/StoneDepthCondition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.CaveSurface import CaveSurface


class StoneDepthCondition(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/material_condition'

    offset: int
    surface_type: CaveSurface
    add_surface_depth: bool
    secondary_depth_range: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::StoneDepthCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "offset",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "surface_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::CaveSurface"
                }
            },
            {
                "kind": "pair",
                "key": "add_surface_depth",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "add_surface_secondary_depth",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "secondary_depth_range",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}
