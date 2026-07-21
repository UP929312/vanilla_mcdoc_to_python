# Generated from symbols.json for ::java::world::component::predicate::AttributeModifiersPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.predicate.AttributeModifiersPredicateEntry import AttributeModifiersPredicateEntry
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate


@dataclass(kw_only=True)
class AttributeModifiersPredicate:
    modifiers: CollectionPredicate[AttributeModifiersPredicateEntry] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::AttributeModifiersPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "modifiers",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::world::component::predicate::CollectionPredicate"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::world::component::predicate::AttributeModifiersPredicateEntry"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

