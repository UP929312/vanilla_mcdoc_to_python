"""
Generated from symbols.json for ::java::assets::item_definition::Special
Local link to file: generated_symbols/assets/item_definition/Special.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.BannerAttachment import BannerAttachment
    from generated_symbols.assets.item_definition.BedPart import BedPart
    from generated_symbols.assets.item_definition.ChestType import ChestType
    from generated_symbols.assets.item_definition.CopperGolemStatuePose import CopperGolemStatuePose
    from generated_symbols.assets.item_definition.EndCubeEffectType import EndCubeEffectType
    from generated_symbols.assets.item_definition.HangingSignAttachment import HangingSignAttachment
    from generated_symbols.assets.item_definition.HeadType import HeadType
    from generated_symbols.assets.item_definition.SpecialModelType import SpecialModelType
    from generated_symbols.assets.item_definition.StandingSignAttachment import StandingSignAttachment
    from generated_symbols.assets.item_definition.WoodType import WoodType
    from generated_symbols.assets.model.ModelRef import ModelRef
    from generated_symbols.util.color.DyeColor import DyeColor
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class ModelStructUnknown:
    type: SpecialModelType


@dataclass(kw_only=True)
class ModelStructBanner:
    type: Literal['minecraft:banner']
    color: DyeColor
    attachment: BannerAttachment | None = None  # Defaults to `ground`.


@dataclass(kw_only=True)
class ModelStructBed:
    type: Literal['minecraft:bed']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/bed/')]
    part: BedPart


@dataclass(kw_only=True)
class ModelStructBook:
    type: Literal['minecraft:book']
    open_angle: float  # Angle in degrees between book cover and book centerline.  `0.0` for closed, `90.0` for open flat.
    page1: float  # The position of the first page inside the book.  `0.0` for leftmost, `1.0` for rightmost.
    page2: float  # The position of the second page inside the book.  `0.0` for leftmost, `1.0` for rightmost.


@dataclass(kw_only=True)
class ModelStructChest:
    type: Literal['minecraft:chest']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/chest/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Defaults to `0`.
    chest_type: ChestType | None = None  # Defaults to `single`.


@dataclass(kw_only=True)
class ModelStructCopperGolemStatue:
    type: Literal['minecraft:copper_golem_statue']
    pose: CopperGolemStatuePose
    texture: str


@dataclass(kw_only=True)
class ModelStructEndCube:
    type: Literal['minecraft:end_cube']
    effect: EndCubeEffectType


@dataclass(kw_only=True)
class ModelStructHangingSign:
    type: Literal['minecraft:hanging_sign']
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/hanging/')] | None = None
    attachment: HangingSignAttachment | None = None  # Defaults to `ceiling_middle`.


@dataclass(kw_only=True)
class ModelStructHead:
    type: Literal['minecraft:head']
    kind: HeadType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/')] | None = None  # Texture to use instead of the texture from `kind`.
    animation: float | None = None  # Controls the animation time for piglin and dragon heads. Defaults to `0`.


@dataclass(kw_only=True)
class ModelStructShulkerBox:
    type: Literal['minecraft:shulker_box']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/shulker/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


@dataclass(kw_only=True)
class ModelStructStandingSign:
    type: Literal['minecraft:standing_sign']
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/')] | None = None
    attachement: StandingSignAttachment | None = None  # There is an extra "e" in the field name. See MC-307498.  Defaults to `ground`.


type ModelStruct = ModelStructUnknown | ModelStructBanner | ModelStructBed | ModelStructBook | ModelStructChest | ModelStructCopperGolemStatue | ModelStructEndCube | ModelStructHangingSign | ModelStructHead | ModelStructShulkerBox | ModelStructStandingSign

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

