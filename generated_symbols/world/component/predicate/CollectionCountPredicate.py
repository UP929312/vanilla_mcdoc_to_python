# Generated from symbols.json for ::java::world::component::predicate::CollectionCountPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


P = TypeVar('P')

@dataclass(kw_only=True)
class CollectionCountPredicate(Generic[P]):
    test: P  # The contents an entry's text must match exactly.
    count: MinMaxBounds[int] | int  # The number of entries that must match the test.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::CollectionCountPredicate": {
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
}

