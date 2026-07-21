# Generated from symbols.json for ::java::util::text::ShowText
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class ShowText:
    value: Text


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ShowText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "attributes": [
                                {
                                    "name": "deprecated",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                }
                            ],
                            "key": "value",
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
                                            "value": "1.16"
                                        }
                                    }
                                }
                            ],
                            "key": "contents",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::text::Text"
                            },
                            "optional": True
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            }
        ]
    }
}

