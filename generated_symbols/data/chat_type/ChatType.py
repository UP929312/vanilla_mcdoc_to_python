"""
Generated from symbols.json for ::java::data::chat_type::ChatType
Local link to file: generated_symbols/data/chat_type/ChatType.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.chat_type.ChatDecoration import ChatDecoration


class ChatType(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'chat_type'

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
