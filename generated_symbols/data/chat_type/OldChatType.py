# Generated from symbols.json for ::java::data::chat_type::OldChatType
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.chat_type.Narration import Narration
    from generated_symbols.data.chat_type.TextDisplay import TextDisplay


@dataclass(kw_only=True)
class OldChatType:
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

