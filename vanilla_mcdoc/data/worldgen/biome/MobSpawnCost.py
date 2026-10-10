"""
Generated from symbols.json for ::java::data::worldgen::biome::MobSpawnCost
Local link to file: generated_symbols/data/worldgen/biome/MobSpawnCost.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class MobSpawnCost(GeneratedModel):
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
