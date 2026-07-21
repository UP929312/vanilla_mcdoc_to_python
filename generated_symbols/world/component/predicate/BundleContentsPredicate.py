# Generated from symbols.json for ::java::world::component::predicate::BundleContentsPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate


@dataclass(kw_only=True)
class BundleContentsPredicate:
    items: CollectionPredicate[ItemPredicate] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::BundleContentsPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "items",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::world::component::predicate::CollectionPredicate"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::ItemPredicate"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

