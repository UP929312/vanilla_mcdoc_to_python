# Generated from symbols.json for ::java::world::block::sign::OldSign
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColor import DyeColor


@dataclass(kw_only=True)
class OldSign(BlockEntity):
    Color: DyeColor | None = None  # Color the text has been dyed.
    GlowingText: bool | None = None
    Text1: str | None = None  # First line of text.
    Text2: str | None = None  # Second line of text.
    Text3: str | None = None  # Third line of text.
    Text4: str | None = None  # Fourth line of text.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::sign::OldSign": {
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
                "desc": "Color the text has been dyed.",
                "key": "Color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::DyeColor"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "GlowingText",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "First line of text.",
                "key": "Text1",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "text_component"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Second line of text.",
                "key": "Text2",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "text_component"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Third line of text.",
                "key": "Text3",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "text_component"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Fourth line of text.",
                "key": "Text4",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "text_component"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

