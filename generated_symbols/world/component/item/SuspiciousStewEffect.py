# Generated from symbols.json for ::java::world::component::item::SuspiciousStewEffect
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class SuspiciousStewEffect:
    id: str
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

