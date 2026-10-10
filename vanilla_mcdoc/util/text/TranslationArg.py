"""
Generated from symbols.json for ::java::util::text::TranslationArg
Local link to file: generated_symbols/util/text/TranslationArg.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


type TranslationArg = Text | bool | int | float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::TranslationArg": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::util::text::Text"
            },
            {
                "kind": "boolean"
            },
            {
                "kind": "byte",
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
                ]
            },
            {
                "kind": "short",
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
                ]
            },
            {
                "kind": "int"
            },
            {
                "kind": "long",
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
                ]
            },
            {
                "kind": "float"
            },
            {
                "kind": "double",
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
                ]
            }
        ]
    }
}
