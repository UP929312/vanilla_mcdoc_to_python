"""
Generated from symbols.json for ::java::assets::item_definition::ModelTint
Local link to file: vanilla_mcdoc/assets/item_definition/ModelTint.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.assets.item_definition.ConstantTint import ConstantTint
from vanilla_mcdoc.assets.item_definition.CustomModelDataTint import CustomModelDataTint
from vanilla_mcdoc.assets.item_definition.DyeTint import DyeTint
from vanilla_mcdoc.assets.item_definition.FireworkTint import FireworkTint
from vanilla_mcdoc.assets.item_definition.GrassTint import GrassTint
from vanilla_mcdoc.assets.item_definition.MapColorTint import MapColorTint
from vanilla_mcdoc.assets.item_definition.PotionTint import PotionTint
from vanilla_mcdoc.assets.item_definition.TeamTint import TeamTint
from vanilla_mcdoc.base import tag_of


class ModelTintConstant(ConstantTint):
    type: Literal['minecraft:constant', 'constant'] = 'minecraft:constant'


class ModelTintCustomModelData(CustomModelDataTint):
    type: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'


class ModelTintDye(DyeTint):
    type: Literal['minecraft:dye', 'dye'] = 'minecraft:dye'


class ModelTintFirework(FireworkTint):
    type: Literal['minecraft:firework', 'firework'] = 'minecraft:firework'


class ModelTintGrass(GrassTint):
    type: Literal['minecraft:grass', 'grass'] = 'minecraft:grass'


class ModelTintMapColor(MapColorTint):
    type: Literal['minecraft:map_color', 'map_color'] = 'minecraft:map_color'


class ModelTintPotion(PotionTint):
    type: Literal['minecraft:potion', 'potion'] = 'minecraft:potion'


class ModelTintTeam(TeamTint):
    type: Literal['minecraft:team', 'team'] = 'minecraft:team'


type ModelTint = Annotated[
    Annotated[ModelTintConstant, Tag('minecraft:constant')]
    | Annotated[ModelTintCustomModelData, Tag('minecraft:custom_model_data')]
    | Annotated[ModelTintDye, Tag('minecraft:dye')]
    | Annotated[ModelTintFirework, Tag('minecraft:firework')]
    | Annotated[ModelTintGrass, Tag('minecraft:grass')]
    | Annotated[ModelTintMapColor, Tag('minecraft:map_color')]
    | Annotated[ModelTintPotion, Tag('minecraft:potion')]
    | Annotated[ModelTintTeam, Tag('minecraft:team')],
    Discriminator(tag_of('type')),
]
