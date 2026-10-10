"""
Generated from symbols.json for ::java::data::advancement::predicate::ParrotPredicate
Local link to file: generated_symbols/data/advancement/predicate/ParrotPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.ParrotVariant import ParrotVariant


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
