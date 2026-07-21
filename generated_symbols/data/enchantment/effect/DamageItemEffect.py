# Generated from symbols.json for ::java::data::enchantment::effect::DamageItemEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class DamageItemEffect:
    amount: LevelBasedValue  # Damage to apply to the enchanted item. The damage is not applied to items held by players in creative mode.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::DamageItemEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Damage to apply to the enchanted item.\nThe damage is not applied to items held by players in creative mode.",
                "key": "amount",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

