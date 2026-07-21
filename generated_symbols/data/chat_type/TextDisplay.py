# Generated from symbols.json for ::java::data::chat_type::TextDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.chat_type.ChatDecoration import ChatDecoration


@dataclass(kw_only=True)
class TextDisplay:
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

