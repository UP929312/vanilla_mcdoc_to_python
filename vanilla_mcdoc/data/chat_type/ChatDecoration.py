"""
Generated from symbols.json for ::java::data::chat_type::ChatDecoration
Local link to file: vanilla_mcdoc/data/chat_type/ChatDecoration.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.chat_type.ChatDecorationParameter import ChatDecorationParameter
    from vanilla_mcdoc.util.text.TextStyle import TextStyle


class ChatDecoration(GeneratedModel):
    translation_key: str
    parameters: list[ChatDecorationParameter]
    style: TextStyle | None = None
