# Generated from symbols.json for ::java::data::chat_type::Narration
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.chat_type.ChatDecoration import ChatDecoration
    from generated_symbols.data.chat_type.NarrationPriority import NarrationPriority


@dataclass(kw_only=True)
class Narration:
    priority: NarrationPriority
    decoration: ChatDecoration | None = None


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

