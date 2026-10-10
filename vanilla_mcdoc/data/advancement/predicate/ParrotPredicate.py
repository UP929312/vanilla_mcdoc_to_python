"""
Generated from symbols.json for ::java::data::advancement::predicate::ParrotPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/ParrotPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.ParrotVariant import ParrotVariant


class ParrotPredicate(GeneratedModel):
    variant: ParrotVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::ParrotPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::ParrotVariant"
                }
            }
        ]
    }
}
