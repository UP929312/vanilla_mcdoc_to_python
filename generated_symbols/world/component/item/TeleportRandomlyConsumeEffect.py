# Generated from symbols.json for ::java::world::component::item::TeleportRandomlyConsumeEffect
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TeleportRandomlyConsumeEffect:
    diameter: Annotated[float, 'Range | Min `1` and above | inclusive'] | None = None  # Defaults to 16.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::TeleportRandomlyConsumeEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 16.",
                "key": "diameter",
                "type": {
                    "kind": "float",
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

