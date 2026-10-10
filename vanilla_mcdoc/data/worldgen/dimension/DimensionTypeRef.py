"""
Generated from symbols.json for ::java::data::worldgen::dimension::DimensionTypeRef
Local link to file: vanilla_mcdoc/data/worldgen/dimension/DimensionTypeRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type DimensionTypeRef = Annotated[str, IdSpec(registry='dimension_type')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::DimensionTypeRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "dimension_type"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "name",
                        "type": {
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
                                                    "value": "dimension_type"
                                                }
                                            },
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
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::dimension::DimensionType"
                        }
                    }
                ],
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
