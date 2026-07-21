# Generated from symbols.json for ::java::util::text::ChangePage
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ChangePage:
    page: Annotated[int, 'Range | Min `1` and above | inclusive']  # The page number to go to.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ChangePage": {
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
                "desc": "The page number to go to.",
                "key": "value",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "integer",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "min": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 1
                                        }
                                    }
                                }
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "The page number to go to.",
                "key": "page",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

