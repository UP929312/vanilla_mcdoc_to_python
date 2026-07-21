# Generated from symbols.json for ::java::data::chat_type::ChatType
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.chat_type.ChatDecoration import ChatDecoration


@dataclass(kw_only=True)
class ChatType:
    chat: ChatDecoration
    narration: ChatDecoration


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::chat_type::ChatType": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "chat",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::ChatDecoration"
                }
            },
            {
                "kind": "pair",
                "key": "narration",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::ChatDecoration"
                }
            }
        ]
    }
}

