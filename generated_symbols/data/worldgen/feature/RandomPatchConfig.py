# Generated from symbols.json for ::java::data::worldgen::feature::RandomPatchConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class RandomPatchConfig:
    feature: FeatureRef
    tries: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # How many attempts will be made to find a placement. Defaults to 128.
    xz_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 7.
    y_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 3.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RandomPatchConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "How many attempts will be made to find a placement. Defaults to 128.",
                "key": "tries",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
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
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "can_replace",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "project",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "need_water",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "xspread",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "int",
                                        "attributes": [
                                            {
                                                "name": "until",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        },
                                        "attributes": [
                                            {
                                                "name": "since",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
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
                            "key": "yspread",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "int",
                                        "attributes": [
                                            {
                                                "name": "until",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        },
                                        "attributes": [
                                            {
                                                "name": "since",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
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
                            "key": "zspread",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "int",
                                        "attributes": [
                                            {
                                                "name": "until",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "int",
                                        "valueRange": {
                                            "kind": 0,
                                            "min": 0
                                        },
                                        "attributes": [
                                            {
                                                "name": "since",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
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
                            "key": "state_provider",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "block_placer",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::BlockPlacer"
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "whitelist",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::util::block_state::BlockState"
                                }
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "blacklist",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::util::block_state::BlockState"
                                }
                            }
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Defaults to 7.",
                            "key": "xz_spread",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to 3.",
                            "key": "y_spread",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "feature",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::feature::FeatureRef"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

