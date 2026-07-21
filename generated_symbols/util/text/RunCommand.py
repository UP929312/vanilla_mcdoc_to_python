# Generated from symbols.json for ::java::util::text::RunCommand
from dataclasses import dataclass


@dataclass(kw_only=True)
class RunCommand:
    command: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::RunCommand": {
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
                                            "value": "1.19.1"
                                        }
                                    }
                                },
                                {
                                    "name": "command",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "slash": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "chat"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.19.1"
                                        }
                                    }
                                },
                                {
                                    "name": "command",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "slash": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "required"
                                                }
                                            }
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
                "key": "command",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "command",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "slash": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "allowed"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

