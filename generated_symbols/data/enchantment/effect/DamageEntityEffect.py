# Generated from symbols.json for ::java::data::enchantment::effect::DamageEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class DamageEntityEffect:
    damage_type: str
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

