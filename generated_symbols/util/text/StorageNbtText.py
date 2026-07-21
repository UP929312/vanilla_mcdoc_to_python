# Generated from symbols.json for ::java::util::text::StorageNbtText
from dataclasses import dataclass
from generated_symbols.util.text.TextNbtBase import TextNbtBase


@dataclass(kw_only=True)
class StorageNbtText(TextNbtBase):
    storage: str
    nbt: str
    source: str | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::StorageNbtText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "storage",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "storage"
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
                                            "storage"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:storage"
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
                        "value": "storage"
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

