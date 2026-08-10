"""
Generated from symbols.json for ::java::world::block::beacon::Beacon
Local link to file: generated_symbols/world/block/beacon/Beacon.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Lockable import Lockable
from generated_symbols.world.block.Nameable import Nameable
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class Beacon(BlockEntity, Nameable, Lockable):
    Levels: int | None = None  # Number of levels from the pyramid.
    primary_effect: Annotated[str, IdSpec(registry='mob_effect')] | None = None
    secondary_effect: Annotated[str, IdSpec(registry='mob_effect')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::beacon::Beacon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Nameable"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Lockable"
                }
            },
            {
                "kind": "pair",
                "desc": "Number of levels from the pyramid.",
                "key": "Levels",
                "type": {
                    "kind": "int"
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "Potion effect.",
                "key": "Primary",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::block::beacon::NoneId"
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::EffectId"
                        }
                    ]
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "Potion effect.",
                "key": "Secondary",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::block::beacon::NoneId"
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::EffectId"
                        }
                    ]
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "key": "primary_effect",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mob_effect"
                                }
                            }
                        }
                    ]
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "key": "secondary_effect",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mob_effect"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

