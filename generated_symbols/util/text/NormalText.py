# Generated from symbols.json for ::java::util::text::NormalText
from dataclasses import dataclass
from generated_symbols.util.text.TextBase import TextBase


@dataclass(kw_only=True)
class NormalText(TextBase):
    text: str
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::NormalText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "text",
                "type": {
                    "kind": "string"
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
                        "value": "text"
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

