# Generated from symbols.json for ::java::data::enchantment::effect::IgniteEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class IgniteEntityEffect:
    duration: LevelBasedValue  # Seconds the fire should last.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::IgniteEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Seconds the fire should last.",
                "key": "duration",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

