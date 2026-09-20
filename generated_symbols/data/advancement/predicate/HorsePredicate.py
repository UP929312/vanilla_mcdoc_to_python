"""
Generated from symbols.json for ::java::data::advancement::predicate::HorsePredicate
Local link to file: generated_symbols/data/advancement/predicate/HorsePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.HorseVariant import HorseVariant


class HorsePredicate(GeneratedModel):
    variant: HorseVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::HorsePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::HorseVariant"
                }
            }
        ]
    }
}

