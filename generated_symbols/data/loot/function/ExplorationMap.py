# Generated from symbols.json for ::java::data::loot::function::ExplorationMap
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class ExplorationMap(Conditions):
    destination: str | list[str]  # Generated structure to locate. Accepts any of the structure types used by the `/locate` command.
    decoration: str | None = None  # The icon used to mark the destination on the map. Accepts any of the map icon text IDs (case insensitive). If `mansion` or `monument` is used, the color of the lines on the item texture changes to match the corresponding explorer map.
    zoom: int | None = None  # Defaults to 2.
    search_radius: int | None = None  # The size, in chunks, of the area to search for structures. The area checked is square, not circular. Radius `0` causes only the current chunk to be searched, radius `1` causes the current chunk and eight adjacent chunks to be searched, and so on. Defaults to `50`.
    skip_existing_chunks: bool | None = None  # Whether to not search in chunks that have already been generated. Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ExplorationMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
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
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Generated structure to locate. Accepts any of the structure types used by the `/locate` command. Defaults to buried treasure.",
                            "key": "destination",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::loot::function::LegacyExplorationMapDestination",
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
                                                        "value": "1.18.2"
                                                    }
                                                }
                                            },
                                            {
                                                "name": "until",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.19"
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
                                                                "value": "worldgen/configured_structure_feature"
                                                            }
                                                        },
                                                        "tags": {
                                                            "kind": "literal",
                                                            "value": {
                                                                "kind": "string",
                                                                "value": "implicit"
                                                            }
                                                        }
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
                                                        "value": "1.19"
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
                                                                "value": "worldgen/structure"
                                                            }
                                                        },
                                                        "tags": {
                                                            "kind": "literal",
                                                            "value": {
                                                                "kind": "string",
                                                                "value": "implicit"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Generated structure to locate. Accepts any of the structure types used by the `/locate` command.",
                            "key": "destination",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
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
                                                                "value": "worldgen/structure"
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
                                                            "value": "worldgen/structure"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The icon used to mark the destination on the map. Accepts any of the map icon text IDs (case insensitive).\nIf `mansion` or `monument` is used, the color of the lines on the item texture changes to match the corresponding explorer map.",
                "key": "decoration",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::function::MapDecoration",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
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
                                            "value": "1.20.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "map_decoration_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to 2.",
                "key": "zoom",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The size, in chunks, of the area to search for structures.\nThe area checked is square, not circular.\nRadius `0` causes only the current chunk to be searched, radius `1` causes the current chunk and eight adjacent chunks to be searched, and so on.\nDefaults to `50`.",
                "key": "search_radius",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to not search in chunks that have already been generated. Defaults to `True`.",
                "key": "skip_existing_chunks",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

