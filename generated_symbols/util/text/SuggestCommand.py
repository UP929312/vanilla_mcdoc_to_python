# Generated from symbols.json for ::java::util::text::SuggestCommand
from dataclasses import dataclass


@dataclass(kw_only=True)
class SuggestCommand:
    command: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::SuggestCommand": {
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
                                    },
                                    "incomplete": {
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
                                            "value": "chat"
                                        }
                                    },
                                    "incomplete": {
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

