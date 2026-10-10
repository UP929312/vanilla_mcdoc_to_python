"""
Generated from symbols.json for ::java::data::enchantment::effect::DamageEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/DamageEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.LevelBasedValue import LevelBasedValue


class DamageEntityEffect(GeneratedModel):
    damage_type: Annotated[str, IdSpec(registry='damage_type')]
    min_damage: LevelBasedValue  # Amount of damage is randomized within the given min/max span.
    max_damage: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::DamageEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "damage_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "damage_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Amount of damage is randomized within the given min/max span.",
                "key": "min_damage",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "max_damage",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}
