"""
Generated from symbols.json for ::java::world::component::item::AttackRange
Local link to file: generated_symbols/world/component/item/AttackRange.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class AttackRange(GeneratedModel):
    min_reach: Annotated[float, Field(ge=0, le=64)] | None = None  # Minimum distance to the target to be considered valid. Defaults to 0.0
    max_reach: Annotated[float, Field(ge=0, le=64)] | None = None  # Maximum distance to the target to be considered valid. Defaults to 3.0
    min_creative_reach: Annotated[float, Field(ge=0, le=64)] | None = None  # Minimum distance from the creative mode attacker to the target to be considered valid. Defaults to 0.0
    max_creative_reach: Annotated[float, Field(ge=0, le=64)] | None = None  # Maximum distance from the creative mode attacker to the target to be considered valid. Defaults to 5.0
    hitbox_margin: Annotated[float, Field(ge=0, le=1)] | None = None  # The margin applied to the target bounding box when checking for valid hitbox collision. Defaults to 0.3
    mob_factor: Annotated[float, Field(ge=0, le=2)] | None = None  # The multiplier applied to `min_reach` and `max_reach` when the user is a mob.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AttackRange": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Minimum distance to the target to be considered valid.\nDefaults to 0.0",
                "key": "min_reach",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum distance to the target to be considered valid.\nDefaults to 3.0",
                "key": "max_reach",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Minimum distance from the creative mode attacker to the target to be considered valid.\nDefaults to 0.0",
                "key": "min_creative_reach",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum distance from the creative mode attacker to the target to be considered valid.\nDefaults to 5.0",
                "key": "max_creative_reach",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The margin applied to the target bounding box when checking for valid hitbox collision.\nDefaults to 0.3",
                "key": "hitbox_margin",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The multiplier applied to `min_reach` and `max_reach` when the user is a mob.",
                "key": "mob_factor",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 2
                    }
                },
                "optional": True
            }
        ]
    }
}

