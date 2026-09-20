"""
Generated from symbols.json for ::java::data::advancement::predicate::RabbitPredicate
Local link to file: generated_symbols/data/advancement/predicate/RabbitPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.RabbitVariant import RabbitVariant


class RabbitPredicate(GeneratedModel):
    variant: RabbitVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::RabbitPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::RabbitVariant"
                }
            }
        ]
    }
}

