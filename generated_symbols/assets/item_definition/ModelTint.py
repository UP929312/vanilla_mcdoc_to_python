"""
Generated from symbols.json for ::java::assets::item_definition::ModelTint
Local link to file: generated_symbols/assets/item_definition/ModelTint.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.assets.item_definition.ConstantTint import ConstantTint
from generated_symbols.assets.item_definition.CustomModelDataTint import CustomModelDataTint
from generated_symbols.assets.item_definition.DyeTint import DyeTint
from generated_symbols.assets.item_definition.FireworkTint import FireworkTint
from generated_symbols.assets.item_definition.GrassTint import GrassTint
from generated_symbols.assets.item_definition.MapColorTint import MapColorTint
from generated_symbols.assets.item_definition.PotionTint import PotionTint
from generated_symbols.assets.item_definition.TeamTint import TeamTint
from pydantic import Field


class ModelTintConstant(ConstantTint):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


class ModelTintCustomModelData(CustomModelDataTint):
    type: Literal['minecraft:custom_model_data'] = 'minecraft:custom_model_data'


class ModelTintDye(DyeTint):
    type: Literal['minecraft:dye'] = 'minecraft:dye'


class ModelTintFirework(FireworkTint):
    type: Literal['minecraft:firework'] = 'minecraft:firework'


class ModelTintGrass(GrassTint):
    type: Literal['minecraft:grass'] = 'minecraft:grass'


class ModelTintMapColor(MapColorTint):
    type: Literal['minecraft:map_color'] = 'minecraft:map_color'


class ModelTintPotion(PotionTint):
    type: Literal['minecraft:potion'] = 'minecraft:potion'


class ModelTintTeam(TeamTint):
    type: Literal['minecraft:team'] = 'minecraft:team'


type ModelTint = Annotated[
    ModelTintConstant | ModelTintCustomModelData | ModelTintDye | ModelTintFirework | ModelTintGrass | ModelTintMapColor | ModelTintPotion | ModelTintTeam,
    Field(discriminator='type'),
]


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

