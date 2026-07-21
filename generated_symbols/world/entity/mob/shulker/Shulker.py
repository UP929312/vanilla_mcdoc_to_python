# Generated from symbols.json for ::java::world::entity::mob::shulker::Shulker
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColorByte import DyeColorByte
    from generated_symbols.world.entity.mob.shulker.AttachFace import AttachFace
    from generated_symbols.world.entity.mob.shulker.ShulkerColor import ShulkerColor


@dataclass(kw_only=True)
class Shulker(MobBase):
    Peek: bool | None = None  # Whether it is peeking.
    AttachFace: AttachFace | None = None  # Which face it is attached to.
    Color: DyeColorByte | ShulkerColor | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::shulker::Shulker": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether it is peeking.",
                "key": "Peek",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Which face it is attached to.",
                "key": "AttachFace",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::shulker::AttachFace"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Color",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::util::color::DyeColorByte"
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::entity::mob::shulker::ShulkerColor"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Approximate x coordinate of the shulker.",
                "key": "APX",
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Approximate y coordinate of the shulker.",
                "key": "APY",
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Approximate z coordinate of the shulker.",
                "key": "APZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

