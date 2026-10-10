"""
Generated from symbols.json for ::java::world::item::suspicious_stew::Effect
Local link to file: generated_symbols/world/item/suspicious_stew/Effect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.EffectId import EffectId


class Effect(GeneratedModel):
    EffectId_: EffectId | None = Field(default=None, alias='EffectId')
    EffectDuration: Annotated[int, Field(ge=1)] | None = None  # Duration in ticks.


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
