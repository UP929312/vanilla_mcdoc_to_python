# Generated from symbols.json for ::java::data::enchantment::effect::ReplaceDiskEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.enchantment.effect.ReplaceBlockEntityEffect import ReplaceBlockEntityEffect

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ReplaceDiskEntityEffect(ReplaceBlockEntityEffect):
    radius: LevelBasedValue
    height: LevelBasedValue
    offset: tuple[int, int, int] | None = None  # Relative coordinates to offset the center of the cylinder by. Defaults to `[0, 0, 0]`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ReplaceDiskEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect::ReplaceBlockEntityEffect"
                }
            },
            {
                "kind": "pair",
                "desc": "Relative coordinates to offset the center of the cylinder by. Defaults to `[0, 0, 0]`.",
                "key": "offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "radius",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

