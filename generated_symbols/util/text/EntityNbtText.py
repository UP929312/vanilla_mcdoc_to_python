# Generated from symbols.json for ::java::util::text::EntityNbtText
from dataclasses import dataclass
from generated_symbols.util.text.TextNbtBase import TextNbtBase


@dataclass(kw_only=True)
class EntityNbtText(TextNbtBase):
    entity: str
    nbt: str
    source: str | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::EntityNbtText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entity",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "entity",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "amount": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "multiple"
                                        }
                                    },
                                    "type": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entities"
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
                                        "kind": "dynamic",
                                        "accessor": [
                                            "entity"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:entity"
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
                        "value": "entity"
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

