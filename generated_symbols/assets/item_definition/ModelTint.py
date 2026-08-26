"""
Generated from symbols.json for ::java::assets::item_definition::ModelTint
Local link to file: generated_symbols/assets/item_definition/ModelTint.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.assets.item_definition.ConstantTint import ConstantTint
from generated_symbols.assets.item_definition.CustomModelDataTint import CustomModelDataTint
from generated_symbols.assets.item_definition.DyeTint import DyeTint
from generated_symbols.assets.item_definition.FireworkTint import FireworkTint
from generated_symbols.assets.item_definition.GrassTint import GrassTint
from generated_symbols.assets.item_definition.MapColorTint import MapColorTint
from generated_symbols.assets.item_definition.PotionTint import PotionTint
from generated_symbols.assets.item_definition.TeamTint import TeamTint


@dataclass(kw_only=True)
class ModelTintConstant(ConstantTint):
    type: Literal['minecraft:constant']


@dataclass(kw_only=True)
class ModelTintCustomModelData(CustomModelDataTint):
    type: Literal['minecraft:custom_model_data']


@dataclass(kw_only=True)
class ModelTintDye(DyeTint):
    type: Literal['minecraft:dye']


@dataclass(kw_only=True)
class ModelTintFirework(FireworkTint):
    type: Literal['minecraft:firework']


@dataclass(kw_only=True)
class ModelTintGrass(GrassTint):
    type: Literal['minecraft:grass']


@dataclass(kw_only=True)
class ModelTintMapColor(MapColorTint):
    type: Literal['minecraft:map_color']


@dataclass(kw_only=True)
class ModelTintPotion(PotionTint):
    type: Literal['minecraft:potion']


@dataclass(kw_only=True)
class ModelTintTeam(TeamTint):
    type: Literal['minecraft:team']


type ModelTint = ModelTintConstant | ModelTintCustomModelData | ModelTintDye | ModelTintFirework | ModelTintGrass | ModelTintMapColor | ModelTintPotion | ModelTintTeam


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ModelTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::TintSourceType",
                    "attributes": [
                        {
                            "name": "id"
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
                    "registry": "minecraft:tint_source"
                }
            }
        ]
    }
}

