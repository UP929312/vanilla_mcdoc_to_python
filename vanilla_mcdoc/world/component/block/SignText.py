"""
Generated from symbols.json for ::java::world::component::block::SignText
Local link to file: vanilla_mcdoc/world/component/block/SignText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColor import DyeColor
    from vanilla_mcdoc.world.component.block.SignLines import SignLines


class SignText(GeneratedModel):
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
