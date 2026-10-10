"""
Generated from symbols.json for ::java::world::block::head::Skull
Local link to file: vanilla_mcdoc/world/block/head/Skull.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from vanilla_mcdoc.util.avatar.Profile import Profile
    from vanilla_mcdoc.util.text.Text import Text


class Skull(BlockEntity):
    ExtraType: str | None = None  # Name of the owner, if exists will be converted to SkullOwner.
    note_block_sound: Annotated[str, IdSpec(registry='weighed_sound_event')] | None = None  # Sound to play when played with a note block. Only works on player head.
    profile: Profile | None = None  # Only works on player head.
    custom_name: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::head::Skull": {
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
                "desc": "Owner of the skull.",
                "key": "Owner",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::head::SkullOwner"
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
                    },
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
                ],
                "key": "SkullOwner",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::head::SkullOwner"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Name of the owner, if exists will be converted to SkullOwner.",
                "key": "ExtraType",
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
                                "value": "1.19.3"
                            }
                        }
                    }
                ],
                "desc": "Sound to play when played with a note block.\nOnly works on player head.",
                "key": "note_block_sound",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "note_block_sound"
                        }
                    ],
                    "registry": "minecraft:data_component"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Only works on player head.",
                "key": "profile",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::avatar::Profile"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "custom_name",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "custom_name"
                        }
                    ],
                    "registry": "minecraft:data_component"
                },
                "optional": True
            }
        ]
    }
}
