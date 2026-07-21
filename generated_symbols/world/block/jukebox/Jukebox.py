# Generated from symbols.json for ::java::world::block::jukebox::Jukebox
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class Jukebox(BlockEntity):
    RecordItem: ItemStack | None = None
    ticks_since_song_started: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::jukebox::Jukebox": {
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
                "key": "RecordItem",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "TickCount",
                            "type": {
                                "kind": "long"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "RecordStartTick",
                            "type": {
                                "kind": "long"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "IsPlaying",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
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
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "ticks_since_song_started",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

