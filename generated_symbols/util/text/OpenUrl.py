# Generated from symbols.json for ::java::util::text::OpenUrl
from dataclasses import dataclass


@dataclass(kw_only=True)
class OpenUrl:
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

