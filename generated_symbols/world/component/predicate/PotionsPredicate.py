# Generated from symbols.json for ::java::world::component::predicate::PotionsPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.EntityEffectsPredicate import EntityEffectsPredicate
    from generated_symbols.world.component.predicate.CollectionPredicate import CollectionPredicate
    from generated_symbols.world.component.predicate.PotionTypeMatch import PotionTypeMatch


@dataclass(kw_only=True)
class PotionsPredicate:
    potions: PotionTypeMatch | None = None
    effects: CollectionPredicate[EntityEffectsPredicate] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::PotionsPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "potions",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::predicate::PotionTypeMatch"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::world::component::predicate::CollectionPredicate"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::EntityEffectsPredicate"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

