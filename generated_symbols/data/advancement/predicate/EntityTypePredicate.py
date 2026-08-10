"""
Generated from symbols.json for ::java::data::advancement::predicate::EntityTypePredicate
Local link to file: generated_symbols/data/advancement/predicate/EntityTypePredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type EntityTypePredicate = Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityTypePredicate": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "entity_type"
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
                                    "value": "entity_type"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

