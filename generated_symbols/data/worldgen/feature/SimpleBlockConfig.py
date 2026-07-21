# Generated from symbols.json for ::java::data::worldgen::feature::SimpleBlockConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class SimpleBlockConfig:
    to_place: BlockStateProvider
    schedule_tick: bool | None = None  # Whether to schedule a block update. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::SimpleBlockConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "to_place",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::util::block_state::BlockState",
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
                            "kind": "reference",
                            "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider",
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
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Whether to schedule a block update. Defaults to `False`.",
                "key": "schedule_tick",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "place_on",
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
                            "key": "place_in",
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
                            "key": "place_under",
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
                                "value": "1.17"
                            }
                        }
                    },
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
                            "key": "place_on",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::util::block_state::BlockState"
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "place_in",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::util::block_state::BlockState"
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "place_under",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::util::block_state::BlockState"
                                }
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

