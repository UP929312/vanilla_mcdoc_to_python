"""
Generated from symbols.json for ::java::world::item::suspicious_stew::Effect
Local link to file: generated_symbols/world/item/suspicious_stew/Effect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.EffectId import EffectId


@dataclass(kw_only=True)
class Effect:
    EffectId: EffectId | None = None
    EffectDuration: Annotated[int, 'Range | `1` and above | inclusive'] | None = None  # Duration in ticks.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::suspicious_stew::Effect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "EffectId",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::EffectId"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Duration in ticks.",
                "key": "EffectDuration",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

