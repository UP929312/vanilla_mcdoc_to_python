# Generated from symbols.json for ::java::assets::lang::LangDeprecated
from dataclasses import dataclass


@dataclass(kw_only=True)
class LangDeprecated:
    removed: list[str]  # List of removed translation keys.
    renamed: dict[str, str]  # Mapping renamed translation keys from old to new keys.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::lang::LangDeprecated": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of removed translation keys.",
                "key": "removed",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "translation_key",
                                "value": {
                                    "kind": "tree",
                                    "values": {
                                        "removed": {
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
                }
            },
            {
                "kind": "pair",
                "desc": "Mapping renamed translation keys from old to new keys.",
                "key": "renamed",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "translation_key",
                                        "value": {
                                            "kind": "tree",
                                            "values": {
                                                "renamed": {
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
                            },
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "translation_key",
                                        "value": {
                                            "kind": "tree",
                                            "values": {
                                                "definition": {
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
                        }
                    ]
                }
            }
        ]
    }
}

