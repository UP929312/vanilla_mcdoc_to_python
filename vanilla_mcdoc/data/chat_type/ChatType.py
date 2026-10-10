"""
Generated from symbols.json for ::java::data::chat_type::ChatType
Local link to file: vanilla_mcdoc/data/chat_type/ChatType.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.chat_type.ChatDecoration import ChatDecoration


class ChatType(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'chat_type'

    chat: ChatDecoration
    narration: ChatDecoration
