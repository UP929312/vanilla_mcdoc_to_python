# Generated from symbols.json for ::java::world::block::creaking_heart::CreakingHeart
from dataclasses import dataclass
from generated_symbols.world.block.BlockEntity import BlockEntity


@dataclass(kw_only=True)
class CreakingHeart(BlockEntity):
    creaking: tuple[int, int, int, int] | None = None  # The creaking mob that is linked to this heart.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::creaking_heart::CreakingHeart": {
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
                "desc": "The creaking mob that is linked to this heart.",
                "key": "creaking",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 4,
                        "max": 4
                    },
                    "attributes": [
                        {
                            "name": "uuid"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

