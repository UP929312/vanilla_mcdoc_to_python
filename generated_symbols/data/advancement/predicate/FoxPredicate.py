"""
Generated from symbols.json for ::java::data::advancement::predicate::FoxPredicate
Local link to file: generated_symbols/data/advancement/predicate/FoxPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.FoxType import FoxType


class FoxPredicate(GeneratedModel):
    variant: FoxType


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::FoxPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::FoxType"
                }
            }
        ]
    }
}

