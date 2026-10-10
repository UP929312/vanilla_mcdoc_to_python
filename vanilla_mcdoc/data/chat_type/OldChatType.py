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
