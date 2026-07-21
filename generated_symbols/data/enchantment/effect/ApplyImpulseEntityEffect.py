# Generated from symbols.json for ::java::data::enchantment::effect::ApplyImpulseEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ApplyImpulseEntityEffect:
    direction: tuple[float, float, float]  # Impulse direction in local coordinates (the same used by `tp @s ^ ^ ^`).  `[left, upward, forward]`
    coordinate_scale: tuple[float, float, float]  # The multipler to apply to the computed impulse direction.  `[x, y, z]`
    magnitude: LevelBasedValue  # The scale of the impulse.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ApplyImpulseEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Impulse direction in local coordinates (the same used by `tp @s ^ ^ ^`). \\\n`[left, upward, forward]`",
                "key": "direction",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "The multipler to apply to the computed impulse direction. \\\n`[x, y, z]`",
                "key": "coordinate_scale",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "The scale of the impulse.",
                "key": "magnitude",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

