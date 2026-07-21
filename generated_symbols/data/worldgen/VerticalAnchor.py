# Generated from symbols.json for ::java::data::worldgen::VerticalAnchor
from dataclasses import dataclass


@dataclass(kw_only=True)
class VerticalAnchorStruct1:
    absolute: int

@dataclass(kw_only=True)
class VerticalAnchorStruct2:
    above_bottom: int

@dataclass(kw_only=True)
class VerticalAnchorStruct3:
    below_top: int

@dataclass(kw_only=True)
class VerticalAnchorStruct4:
    relative_to_sea_level: int

type VerticalAnchor = VerticalAnchorStruct1 | VerticalAnchorStruct2 | VerticalAnchorStruct3 | VerticalAnchorStruct4


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::VerticalAnchor": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "absolute",
                        "type": {
                            "kind": "int"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "above_bottom",
                        "type": {
                            "kind": "int"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "below_top",
                        "type": {
                            "kind": "int"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "relative_to_sea_level",
                        "type": {
                            "kind": "int"
                        }
                    }
                ],
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

