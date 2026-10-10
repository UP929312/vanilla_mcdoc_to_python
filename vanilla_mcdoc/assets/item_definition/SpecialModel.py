"""
Generated from symbols.json for ::java::assets::item_definition::SpecialModel
Local link to file: vanilla_mcdoc/assets/item_definition/SpecialModel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.assets.item_definition.Banner import Banner
from vanilla_mcdoc.assets.item_definition.Book import Book
from vanilla_mcdoc.assets.item_definition.Chest import Chest
from vanilla_mcdoc.assets.item_definition.CopperGolemStatue import CopperGolemStatue
from vanilla_mcdoc.assets.item_definition.EndCube import EndCube
from vanilla_mcdoc.assets.item_definition.Head import Head
from vanilla_mcdoc.assets.item_definition.ShulkerBox import ShulkerBox
from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.SpecialModelType import SpecialModelType


class SpecialModelUnknown(GeneratedModel):
    type: SpecialModelType


class SpecialModelBanner(Banner):
    type: Literal['minecraft:banner', 'banner'] = 'minecraft:banner'


class SpecialModelBook(Book):
    type: Literal['minecraft:book', 'book'] = 'minecraft:book'


class SpecialModelChest(Chest):
    type: Literal['minecraft:chest', 'chest'] = 'minecraft:chest'


class SpecialModelCopperGolemStatue(CopperGolemStatue):
    type: Literal['minecraft:copper_golem_statue', 'copper_golem_statue'] = 'minecraft:copper_golem_statue'


class SpecialModelEndCube(EndCube):
    type: Literal['minecraft:end_cube', 'end_cube'] = 'minecraft:end_cube'


class SpecialModelHead(Head):
    type: Literal['minecraft:head', 'head'] = 'minecraft:head'


class SpecialModelShulkerBox(ShulkerBox):
    type: Literal['minecraft:shulker_box', 'shulker_box'] = 'minecraft:shulker_box'


type SpecialModel = SpecialModelUnknown | SpecialModelBanner | SpecialModelBook | SpecialModelChest | SpecialModelCopperGolemStatue | SpecialModelEndCube | SpecialModelHead | SpecialModelShulkerBox


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::SpecialModel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::SpecialModelType",
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
                    "registry": "minecraft:special_item_model"
                }
            }
        ]
    }
}
