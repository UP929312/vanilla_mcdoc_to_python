# Generated from symbols.json for ::java::data::worldgen::biome::MobSpawnCost
from dataclasses import dataclass


@dataclass(kw_only=True)
class MobSpawnCost:
    energy_budget: float
    charge: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::MobSpawnCost": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "energy_budget",
                "type": {
                    "kind": "double"
                }
            },
            {
                "kind": "pair",
                "key": "charge",
                "type": {
                    "kind": "double"
                }
            }
        ]
    }
}

