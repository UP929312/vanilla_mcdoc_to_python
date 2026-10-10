"""
Generated from symbols.json for ::java::util::avatar::ProfileProperty
Local link to file: generated_symbols/util/avatar/ProfileProperty.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class ProfileProperty(GeneratedModel):
    name: Annotated[str, Field(min_length=0, max_length=64)]  # Usually `textures`.
    value: Annotated[str, Field(min_length=0, max_length=32767)]  # Base64 encoded JSON value of the texture index.
    signature: Annotated[str, Field(min_length=0, max_length=1024)] | None = None  # Verifies the hash of the resulting texture.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::avatar::ProfileProperty": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Usually `textures`.",
                "key": "name",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "lengthRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 64
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Base64 encoded JSON value of the texture index.",
                "key": "value",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "lengthRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 32767
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Verifies the hash of the resulting texture.",
                "key": "signature",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "lengthRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 1024
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

