"""
Generated from symbols.json for ::java::data::chat_type::TextDisplay
Local link to file: vanilla_mcdoc/data/chat_type/TextDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.chat_type.ChatDecoration import ChatDecoration


class TextDisplay(GeneratedModel):
    decoration: ChatDecoration | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::chat_type::TextDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "decoration",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::ChatDecoration"
                },
                "optional": True
            }
        ]
    }
}
