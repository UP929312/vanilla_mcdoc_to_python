"""
Generated from symbols.json for ::java::util::text::ChangePage
Local link to file: generated_symbols/util/text/ChangePage.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class ChangePage(GeneratedModel):
    page: Annotated[int, Field(ge=1)]  # The page number to go to.


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

