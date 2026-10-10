"""
Generated from symbols.json for ::java::data::chat_type::OldChatType
Local link to file: vanilla_mcdoc/data/chat_type/OldChatType.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.chat_type.Narration import Narration
    from vanilla_mcdoc.data.chat_type.TextDisplay import TextDisplay


class OldChatType(GeneratedModel):
    chat: TextDisplay | None = None
    overlay: TextDisplay | None = None
    narration: Narration | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::chat_type::OldChatType": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "chat",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::TextDisplay"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "overlay",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::TextDisplay"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "narration",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::Narration"
                },
                "optional": True
            }
        ]
    }
}
