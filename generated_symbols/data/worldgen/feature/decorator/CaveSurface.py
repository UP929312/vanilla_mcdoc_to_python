# Generated from symbols.json for ::java::data::worldgen::feature::decorator::CaveSurface
from dataclasses import dataclass


@dataclass(kw_only=True)
class CaveSurface:
    surface: str
    floor_to_ceiling_search_range: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::decorator::CaveSurface": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "surface",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "floor"
                            }
                        },
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "ceiling"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "floor_to_ceiling_search_range",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

