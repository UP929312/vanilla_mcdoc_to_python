"""
Generated from symbols.json for ::java::assets::item_definition::SpecialModel
Local link to file: generated_symbols/assets/item_definition/SpecialModel.py
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
    from generated_symbols.util.color.DyeColor import DyeColor


@dataclass(kw_only=True)
class SpecialModelUnknown:
    type: SpecialModelType


@dataclass(kw_only=True)
class SpecialModelBanner:
    type: Literal['minecraft:banner']
    color: DyeColor
    attachment: BannerAttachment | None = None  # Defaults to `ground`.


@dataclass(kw_only=True)
class SpecialModelBed:
    type: Literal['minecraft:bed']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/bed/')]
    part: BedPart


@dataclass(kw_only=True)
class SpecialModelBook:
    type: Literal['minecraft:book']
    open_angle: float  # Angle in degrees between book cover and book centerline.  `0.0` for closed, `90.0` for open flat.
    page1: float  # The position of the first page inside the book.  `0.0` for leftmost, `1.0` for rightmost.
    page2: float  # The position of the second page inside the book.  `0.0` for leftmost, `1.0` for rightmost.


@dataclass(kw_only=True)
class SpecialModelChest:
    type: Literal['minecraft:chest']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/chest/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Defaults to `0`.
    chest_type: ChestType | None = None  # Defaults to `single`.


@dataclass(kw_only=True)
class SpecialModelCopperGolemStatue:
    type: Literal['minecraft:copper_golem_statue']
    pose: CopperGolemStatuePose
    texture: str


@dataclass(kw_only=True)
class SpecialModelEndCube:
    type: Literal['minecraft:end_cube']
    effect: EndCubeEffectType


@dataclass(kw_only=True)
class SpecialModelHangingSign:
    type: Literal['minecraft:hanging_sign']
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/hanging/')] | None = None
    attachment: HangingSignAttachment | None = None  # Defaults to `ceiling_middle`.


@dataclass(kw_only=True)
class SpecialModelHead:
    type: Literal['minecraft:head']
    kind: HeadType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/')] | None = None  # Texture to use instead of the texture from `kind`.
    animation: float | None = None  # Controls the animation time for piglin and dragon heads. Defaults to `0`.


@dataclass(kw_only=True)
class SpecialModelShulkerBox:
    type: Literal['minecraft:shulker_box']
    texture: Annotated[str, IdSpec(registry='texture', path='entity/shulker/')]
    openness: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None


@dataclass(kw_only=True)
class SpecialModelStandingSign:
    type: Literal['minecraft:standing_sign']
    wood_type: WoodType
    texture: Annotated[str, IdSpec(registry='texture', path='entity/signs/')] | None = None
    attachement: StandingSignAttachment | None = None  # There is an extra "e" in the field name. See MC-307498.  Defaults to `ground`.


type SpecialModel = SpecialModelUnknown | SpecialModelBanner | SpecialModelBed | SpecialModelBook | SpecialModelChest | SpecialModelCopperGolemStatue | SpecialModelEndCube | SpecialModelHangingSign | SpecialModelHead | SpecialModelShulkerBox | SpecialModelStandingSign


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

