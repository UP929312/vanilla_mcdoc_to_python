"""
Generated from symbols.json for ::java::util::text::OpenUrl
Local link to file: generated_symbols/util/text/OpenUrl.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class OpenUrl(GeneratedModel):
    url: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::OpenUrl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                "key": "value",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "url"
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
                "key": "url",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "url"
                        }
                    ]
                }
            }
        ]
    }
}

