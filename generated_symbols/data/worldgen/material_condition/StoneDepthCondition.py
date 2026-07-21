# Generated from symbols.json for ::java::data::worldgen::material_condition::StoneDepthCondition
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CaveSurface import CaveSurface


@dataclass(kw_only=True)
class StoneDepthCondition:
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

