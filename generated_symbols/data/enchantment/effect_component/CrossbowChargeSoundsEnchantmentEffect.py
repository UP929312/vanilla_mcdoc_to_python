# Generated from symbols.json for ::java::data::enchantment::effect_component::CrossbowChargeSoundsEnchantmentEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class CrossbowChargeSoundsEnchantmentEffect:
    start: SoundEventRef | None = None  # Start of charging.
    mid: SoundEventRef | None = None  # Middle of charging.
    end: SoundEventRef | None = None  # End of charging.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::CrossbowChargeSoundsEnchantmentEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Start of charging.",
                "key": "start",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Middle of charging.",
                "key": "mid",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "End of charging.",
                "key": "end",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            }
        ]
    }
}

