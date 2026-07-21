# Generated from symbols.json for ::java::util::text::TranslatedText
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class TranslatedText(TextBase):
    translate: str
    fallback: str | None = None
    with_: Annotated[list[Text], 'Length = 1 (inclusive) and above'] | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::TranslatedText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "translate",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "translation_key"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.4"
                            }
                        }
                    }
                ],
                "key": "fallback",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "translation_value"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "with",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::text::Text"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "translatable"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextBase"
                }
            }
        ]
    }
}

