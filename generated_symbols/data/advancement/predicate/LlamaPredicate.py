"""
Generated from symbols.json for ::java::data::advancement::predicate::LlamaPredicate
Local link to file: generated_symbols/data/advancement/predicate/LlamaPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.LlamaVariant import LlamaVariant


class LlamaPredicate(GeneratedModel):
    variant: LlamaVariant


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LlamaPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::LlamaVariant"
                }
            }
        ]
    }
}

