# Generated from symbols.json for ::java::world::component::predicate::WrittenBookPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate


@dataclass(kw_only=True)
class WrittenBookPredicate:
    pages: CollectionPredicate[Text] | None = None  # Matches the raw text, instead of filtered.
    author: str | None = None
    title: str | None = None
    generation: MinMaxBounds[int] | int | None = None
    resolved: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::WrittenBookPredicate": {
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
                            "kind": "reference",
                            "path": "::java::util::text::Text"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "author",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "title",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "generation",
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
            },
            {
                "kind": "pair",
                "key": "resolved",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

