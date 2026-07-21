# Generated from symbols.json for ::java::util::text::ScoreText
from dataclasses import dataclass
from typing import Any
from generated_symbols.util.text.TextBase import TextBase


@dataclass(kw_only=True)
class ScoreText(TextBase):
    score: Any
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ScoreText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "score",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "objective",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "objective"
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "score_holder"
                                    }
                                ]
                            }
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
                        "value": "score"
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

