"""
Generated from symbols.json for ::java::world::component::predicate::BundleContentsPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/BundleContentsPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate


class BundleContentsPredicate(GeneratedModel):
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
