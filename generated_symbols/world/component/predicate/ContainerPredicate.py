"""
Generated from symbols.json for ::java::world::component::predicate::ContainerPredicate
Local link to file: generated_symbols/world/component/predicate/ContainerPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate


class ContainerPredicate(GeneratedModel):
    items: CollectionPredicate[ItemPredicate] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::ContainerPredicate": {
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
