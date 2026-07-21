# Generated from symbols.json for ::java::data::advancement::predicate::EntityTagPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class EntityTagPredicate:
    any_of: list[str] | None = None  # Must have at least one of the listed tags.
    all_of: list[str] | None = None  # Must have all the listed tags.
    none_of: list[str] | None = None  # Must have none of the listed tags.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityTagPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Must have at least one of the listed tags.",
                "key": "any_of",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "tag"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Must have all the listed tags.",
                "key": "all_of",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "tag"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Must have none of the listed tags.",
                "key": "none_of",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "tag"
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

