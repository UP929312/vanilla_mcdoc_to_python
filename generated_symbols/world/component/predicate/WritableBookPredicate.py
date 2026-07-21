# Generated from symbols.json for ::java::world::component::predicate::WritableBookPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate


@dataclass(kw_only=True)
class WritableBookPredicate:
    pages: CollectionPredicate[str] | None = None  # Matches the raw text, instead of filtered.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::WritableBookPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Matches the raw text, instead of filtered.",
                "key": "pages",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::world::component::predicate::CollectionPredicate"
                    },
                    "typeArgs": [
                        {
                            "kind": "string"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

