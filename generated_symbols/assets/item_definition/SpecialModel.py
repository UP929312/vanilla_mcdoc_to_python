"""
Generated from symbols.json for ::java::assets::item_definition::SpecialModel
Local link to file: generated_symbols/assets/item_definition/SpecialModel.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.assets.item_definition.Banner import Banner
from generated_symbols.assets.item_definition.Book import Book
from generated_symbols.assets.item_definition.Chest import Chest
from generated_symbols.assets.item_definition.CopperGolemStatue import CopperGolemStatue
from generated_symbols.assets.item_definition.EndCube import EndCube
from generated_symbols.assets.item_definition.Head import Head
from generated_symbols.assets.item_definition.ShulkerBox import ShulkerBox

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.SpecialModelType import SpecialModelType


@dataclass(kw_only=True)
class SpecialModelUnknown:
    type: SpecialModelType


@dataclass(kw_only=True)
class SpecialModelBanner(Banner):
    type: Literal['minecraft:banner'] = 'minecraft:banner'


@dataclass(kw_only=True)
class SpecialModelBook(Book):
    type: Literal['minecraft:book'] = 'minecraft:book'


@dataclass(kw_only=True)
class SpecialModelChest(Chest):
    type: Literal['minecraft:chest'] = 'minecraft:chest'


@dataclass(kw_only=True)
class SpecialModelCopperGolemStatue(CopperGolemStatue):
    type: Literal['minecraft:copper_golem_statue'] = 'minecraft:copper_golem_statue'


@dataclass(kw_only=True)
class SpecialModelEndCube(EndCube):
    type: Literal['minecraft:end_cube'] = 'minecraft:end_cube'


@dataclass(kw_only=True)
class SpecialModelHead(Head):
    type: Literal['minecraft:head'] = 'minecraft:head'


@dataclass(kw_only=True)
class SpecialModelShulkerBox(ShulkerBox):
    type: Literal['minecraft:shulker_box'] = 'minecraft:shulker_box'


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

