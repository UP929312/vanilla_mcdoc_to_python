"""
Generated from symbols.json for ::java::data::advancement::predicate::DamageTagPredicate
Local link to file: generated_symbols/data/advancement/predicate/DamageTagPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class DamageTagPredicate:
    id: Annotated[str, IdSpec(registry='damage_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='damage_type')]]
    expected: bool  # Whether the damage is expected to have or not have the tag.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::DamageTagPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
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
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "damage_type"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "implicit"
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
                                            "value": "26.3"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "damage_type"
                                                }
                                            },
                                            "tags": {
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
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "damage_type"
                                            }
                                        }
                                    }
                                ]
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
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
                "desc": "Whether the damage is expected to have or not have the tag.",
                "key": "expected",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

