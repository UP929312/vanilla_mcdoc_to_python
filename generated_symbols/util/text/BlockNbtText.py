# Generated from symbols.json for ::java::util::text::BlockNbtText
from dataclasses import dataclass
from generated_symbols.util.text.TextNbtBase import TextNbtBase


@dataclass(kw_only=True)
class BlockNbtText(TextNbtBase):
    block: str
    nbt: str
    source: str | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::BlockNbtText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "vector",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "dimension": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 3
                                        }
                                    },
                                    "integer": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "boolean",
                                            "value": True
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
                "key": "nbt",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "nbt_path",
                            "value": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "static",
                                        "value": "%fallback"
                                    }
                                ],
                                "registry": "minecraft:block"
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "source",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "block"
                    }
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
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "nbt"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextNbtBase"
                }
            }
        ]
    }
}

