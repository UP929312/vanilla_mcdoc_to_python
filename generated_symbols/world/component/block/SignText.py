# Generated from symbols.json for ::java::world::component::block::SignText
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColor import DyeColor
    from generated_symbols.world.component.block.SignLines import SignLines


@dataclass(kw_only=True)
class SignText:
    messages: SignLines
    filtered_messages: SignLines | None = None  # Shown to players with the profanity filter enabled on Realms.
    color: DyeColor | None = None
    has_glowing_text: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::SignText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "messages",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::block::SignLines"
                }
            },
            {
                "kind": "pair",
                "desc": "Shown to players with the profanity filter enabled on Realms.",
                "key": "filtered_messages",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::block::SignLines"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::DyeColor"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "has_glowing_text",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

