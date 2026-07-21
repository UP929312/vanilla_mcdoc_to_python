# Generated from symbols.json for ::java::util::text::SelectorText
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SelectorText(TextBase):
    selector: str
    separator: Text | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::SelectorText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "selector",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "entity"
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "separator",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
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
                        "value": "selector"
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

