# Generated from symbols.json for ::java::world::component::predicate::CollectionPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


P = TypeVar('P')

@dataclass(kw_only=True)
class CollectionPredicate(Generic[P]):
    contains: list[P] | None = None  # A list of tests. For each test, there must be at least one entry whose contents match exactly.
    count: list[Any] | None = None
    size: MinMaxBounds[int] | int | None = None  # When set, total number of entries in the this collection.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::CollectionPredicate": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "desc": "A list of tests. For each test, there must be at least one entry whose contents match exactly.",
                    "key": "contains",
                    "type": {
                        "kind": "list",
                        "item": {
                            "kind": "reference",
                            "path": "::java::world::component::predicate::P"
                        }
                    },
                    "optional": True
                },
                {
                    "kind": "pair",
                    "key": "count",
                    "type": {
                        "kind": "list",
                        "item": {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "desc": "The contents an entry's text must match exactly.",
                                    "key": "test",
                                    "type": {
                                        "kind": "reference",
                                        "path": "::java::world::component::predicate::P"
                                    }
                                },
                                {
                                    "kind": "pair",
                                    "desc": "The number of entries that must match the test.",
                                    "key": "count",
                                    "type": {
                                        "kind": "concrete",
                                        "child": {
                                            "kind": "reference",
                                            "path": "::java::data::util::MinMaxBounds"
                                        },
                                        "typeArgs": [
                                            {
                                                "kind": "int"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    },
                    "optional": True
                },
                {
                    "kind": "pair",
                    "desc": "When set, total number of entries in the this collection.",
                    "key": "size",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::data::util::MinMaxBounds"
                        },
                        "typeArgs": [
                            {
                                "kind": "int"
                            }
                        ]
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::world::component::predicate::P"
            }
        ]
    }
}

