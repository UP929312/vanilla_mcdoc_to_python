"""
Generated from symbols.json for ::java::data::variants::SpawnCondition
Local link to file: generated_symbols/data/variants/SpawnCondition.py
"""
# ~~~ CODE ~~~
from typing import Literal

from generated_symbols.data.variants.BiomeCheck import BiomeCheck
from generated_symbols.data.variants.MoonBrightnessCheck import MoonBrightnessCheck
from generated_symbols.data.variants.StructureCheck import StructureCheck


class SpawnConditionBiome(BiomeCheck):
    type: Literal['minecraft:biome'] = 'minecraft:biome'


class SpawnConditionMoonBrightness(MoonBrightnessCheck):
    type: Literal['minecraft:moon_brightness'] = 'minecraft:moon_brightness'


class SpawnConditionStructure(StructureCheck):
    type: Literal['minecraft:structure'] = 'minecraft:structure'


type SpawnCondition = SpawnConditionBiome | SpawnConditionMoonBrightness | SpawnConditionStructure


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::SpawnCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "spawn_condition_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:spawn_condition"
                }
            }
        ]
    }
}

