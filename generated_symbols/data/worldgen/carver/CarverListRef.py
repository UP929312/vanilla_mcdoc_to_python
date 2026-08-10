"""
Generated from symbols.json for ::java::data::worldgen::carver::CarverListRef
Local link to file: generated_symbols/data/worldgen/carver/CarverListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver


type CarverListRef = ConfiguredCarver | Annotated[str, IdSpec(registry='worldgen/carver', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/carver')] | ConfiguredCarver]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CarverListRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::carver::ConfiguredCarver"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::carver::ConfiguredCarver"
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "worldgen/configured_carver"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/configured_carver"
                                }
                            }
                        }
                    ]
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "string",
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
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "worldgen/carver"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
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
                                            "value": "worldgen/carver"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::carver::ConfiguredCarver"
                        }
                    ]
                },
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

