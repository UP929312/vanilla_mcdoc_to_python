# Generated from symbols.json for ::java::world::entity::painting::Painting
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.BlockAttachedEntity import BlockAttachedEntity

if TYPE_CHECKING:
    from generated_symbols.world.entity.painting.Facing import Facing


@dataclass(kw_only=True)
class Painting(BlockAttachedEntity):
    facing: Facing | None = None  # Direction it is facing.
    variant: str | None = None  # Type of painting.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::painting::Painting": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::BlockAttachedEntity"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Direction it is facing.",
                "key": "Facing",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::painting::Facing"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Direction it is facing.",
                "key": "facing",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::painting::Facing"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Type of painting.",
                "key": "Motive",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "motive"
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
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "desc": "Type of painting.",
                "key": "variant",
                "type": {
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
                                            "value": "painting_variant"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::variants::painting::PaintingVariant",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21"
                                        }
                                    }
                                },
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.6"
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
}

