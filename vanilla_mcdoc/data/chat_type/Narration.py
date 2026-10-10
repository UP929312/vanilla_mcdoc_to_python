"""
Generated from symbols.json for ::java::data::chat_type::Narration
Local link to file: vanilla_mcdoc/data/chat_type/Narration.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.chat_type.ChatDecoration import ChatDecoration
    from vanilla_mcdoc.data.chat_type.NarrationPriority import NarrationPriority


class Narration(GeneratedModel):
    decoration: ChatDecoration | None = None
    priority: NarrationPriority


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::chat_type::Narration": {
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
            },
            {
                "kind": "pair",
                "key": "priority",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::chat_type::NarrationPriority"
                }
            }
        ]
    }
}
