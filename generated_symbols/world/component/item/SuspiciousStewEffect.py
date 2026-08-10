"""
Generated from symbols.json for ::java::world::component::item::SuspiciousStewEffect
Local link to file: generated_symbols/world/component/item/SuspiciousStewEffect.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class SuspiciousStewEffect:
    id: Annotated[str, IdSpec(registry='mob_effect')]
    duration: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Duration of the effect in ticks. Defaults to `160`; 8 seconds.


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

