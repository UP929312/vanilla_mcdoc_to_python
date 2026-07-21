# Generated from symbols.json for ::java::world::block::jigsaw::Jigsaw
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.block.jigsaw.JointType import JointType


@dataclass(kw_only=True)
class Jigsaw:
    joint: JointType | None = None  # How the resultant structure can be transformed.
    pool: str | None = None  # Structure pool this will "spawn" in.
    name: str | None = None  # ID this will "spawn" in.
    target: str | None = None  # ID of the type of jigsaw this will be "spawned" from.
    final_state: str | None = None  # Final block state of the jigsaw.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::jigsaw::Jigsaw": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Structure pool this will connect to.",
                "key": "target_pool",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/template_pool"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "How the resultant structure can be transformed.",
                "key": "joint",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::jigsaw::JointType"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "Structure pool this will \"spawn\" in.",
                "key": "pool",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/template_pool"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "ID this will \"spawn\" in.",
                "key": "name",
                "type": {
                    "kind": "string"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "ID of the type of jigsaw this will be \"spawned\" from.",
                "key": "target",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Final block state of the jigsaw.",
                "key": "final_state",
                "type": {
                    "kind": "string"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "desc": "ID of the type of jigsaw this connects to.",
                "key": "attachment_type",
                "type": {
                    "kind": "string"
                },
                "optional": True
            }
        ]
    }
}

