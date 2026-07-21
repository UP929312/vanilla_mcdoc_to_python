# Generated from symbols.json for ::java::data::advancement::predicate::EntityEffectsPredicate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.MobEffectPredicate import MobEffectPredicate


type EntityEffectsPredicate = dict[str, MobEffectPredicate]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntityEffectsPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mob_effect"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::MobEffectPredicate"
                }
            }
        ]
    }
}

