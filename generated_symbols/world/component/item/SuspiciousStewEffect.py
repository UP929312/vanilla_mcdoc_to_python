"""
Generated from symbols.json for ::java::world::component::item::SuspiciousStewEffect
Local link to file: generated_symbols/world/component/item/SuspiciousStewEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


class SuspiciousStewEffect(GeneratedModel):
    id: Annotated[str, IdSpec(registry='mob_effect')]
    duration: Annotated[int, Field(ge=1)] | None = None  # Duration of the effect in ticks. Defaults to `160`; 8 seconds.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::SuspiciousStewEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mob_effect"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Duration of the effect in ticks. Defaults to `160`; 8 seconds.",
                "key": "duration",
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

