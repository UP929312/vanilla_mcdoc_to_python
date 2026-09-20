"""
Generated from symbols.json for ::java::data::advancement::predicate::AxolotlPredicate
Local link to file: generated_symbols/data/advancement/predicate/AxolotlPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.AxolotlVariant import AxolotlVariant


class AxolotlPredicate(GeneratedModel):
    variant: AxolotlVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::AxolotlPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::AxolotlVariant"
                }
            }
        ]
    }
}

