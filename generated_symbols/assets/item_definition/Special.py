"""
Generated from symbols.json for ::java::assets::item_definition::Special
Local link to file: generated_symbols/assets/item_definition/Special.py
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
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class ModelStructUnknown:
    type: SpecialModelType


@dataclass(kw_only=True)
class ModelStructBanner(Banner):
    type: Literal['minecraft:banner']


@dataclass(kw_only=True)
class ModelStructBook(Book):
    type: Literal['minecraft:book']


@dataclass(kw_only=True)
class ModelStructChest(Chest):
    type: Literal['minecraft:chest']


@dataclass(kw_only=True)
class ModelStructCopperGolemStatue(CopperGolemStatue):
    type: Literal['minecraft:copper_golem_statue']


@dataclass(kw_only=True)
class ModelStructEndCube(EndCube):
    type: Literal['minecraft:end_cube']


@dataclass(kw_only=True)
class ModelStructHead(Head):
    type: Literal['minecraft:head']


@dataclass(kw_only=True)
class ModelStructShulkerBox(ShulkerBox):
    type: Literal['minecraft:shulker_box']


type ModelStruct = ModelStructUnknown | ModelStructBanner | ModelStructBook | ModelStructChest | ModelStructCopperGolemStatue | ModelStructEndCube | ModelStructHead | ModelStructShulkerBox

@dataclass(kw_only=True)
class Special:
    model: ModelStruct  # Renders a special hardcoded model.
    base: ModelRef  # Base model, providing transformations, particle texture and GUI light.
    transformation: Transformation | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Special": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Renders a special hardcoded model.",
                "key": "model",
                "type": {
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
            },
            {
                "kind": "pair",
                "desc": "Base model, providing transformations, particle texture and GUI light.",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::model::ModelRef"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "transformation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Transformation"
                },
                "optional": True
            }
        ]
    }
}

