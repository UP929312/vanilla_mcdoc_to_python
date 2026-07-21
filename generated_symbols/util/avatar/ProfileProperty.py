# Generated from symbols.json for ::java::util::avatar::ProfileProperty
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ProfileProperty:
    name: Annotated[str, 'Length = 0-64 (both inclusive)']  # Usually `textures`.
    value: Annotated[str, 'Length = 0-32767 (both inclusive)']  # Base64 encoded JSON value of the texture index.
    signature: Annotated[str, 'Length = 0-1024 (both inclusive)'] | None = None  # Verifies the hash of the resulting texture.


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

