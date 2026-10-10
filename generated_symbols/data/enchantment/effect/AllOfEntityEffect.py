"""
Generated from symbols.json for ::java::data::enchantment::effect::AllOfEntityEffect
Local link to file: generated_symbols/data/enchantment/effect/AllOfEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect


class AllOfEntityEffect(GeneratedModel):
    effects: Annotated[list[EntityEffect], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AllOfEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::EntityEffect"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

