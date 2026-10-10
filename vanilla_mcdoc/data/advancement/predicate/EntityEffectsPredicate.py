"""
Generated from symbols.json for ::java::data::advancement::predicate::EntityEffectsPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EntityEffectsPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.MobEffectPredicate import MobEffectPredicate


type EntityEffectsPredicate = dict[Annotated[str, IdSpec(registry='mob_effect')], MobEffectPredicate]


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
