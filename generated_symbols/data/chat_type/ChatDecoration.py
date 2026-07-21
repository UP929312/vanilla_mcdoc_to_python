# Generated from symbols.json for ::java::data::chat_type::ChatDecoration
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.chat_type.ChatDecorationParameter import ChatDecorationParameter
    from generated_symbols.util.text.TextStyle import TextStyle


@dataclass(kw_only=True)
class ChatDecoration:
    translation_key: str
    parameters: list[ChatDecorationParameter]
    style: TextStyle | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::chat_type::ChatDecoration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "translation_key",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "parameters",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::chat_type::ChatDecorationParameter"
                    }
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "style",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::text::TextStyle"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "style",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::text::TextStyle"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

