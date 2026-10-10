"""
Generated from symbols.json for ::java::assets::texture_meta::TextureMeta
Local link to file: vanilla_mcdoc/assets/texture_meta/TextureMeta.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.PaletteRef import PaletteRef
    from vanilla_mcdoc.assets.texture_meta.GuiSpriteScaling import GuiSpriteScaling
    from vanilla_mcdoc.assets.texture_meta.MipmapStrategy import MipmapStrategy
    from vanilla_mcdoc.assets.texture_meta.VillagerHatType import VillagerHatType


class FramesStruct(GeneratedModel):
    index: Annotated[int, Field(ge=0)]  # A number corresponding to position of a frame from the top, with the top frame being 0.
    time: Annotated[int, Field(ge=1)] | None = None  # The time in ticks to show this frame, overriding `frametime` above.


class AnimationStruct(GeneratedModel):
    interpolate: bool | None = None  # If true, additional frames will be generated between frames with a frame time greater than 1 between them. Defaults to false.
    width: Annotated[int, Field(ge=1)] | None = None  # The width of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.
    height: Annotated[int, Field(ge=1)] | None = None  # The height of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.
    frametime: Annotated[int, Field(ge=1)] | None = None  # Sets the default time for each frame in increments of one game tick. Defaults to 1.
    frames: list[FramesStruct | Annotated[int, Field(ge=0)]] | None = None  # Defaults to displaying all the frames from top to bottom.


class GuiStruct(GeneratedModel):
    scaling: GuiSpriteScaling | None = None  # Configures how the GUI texture should be scaled. Defaults to `stretch`.


class VillagerStruct(GeneratedModel):
    hat: VillagerHatType | None = None  # Determines whether the villager's 'profession' hat layer should allow the 'type' hat layer to render or not.  Defaults to `none`.


class TextureStruct(GeneratedModel):
    blur: bool | None = None  # Causes the texture to blur when viewed from close up. Defaults to false.
    clamp: bool | None = None  # Causes the texture to stretch instead of tiling in cases where it otherwise would, such as on the shadow. Defaults to false.
    mipmap_strategy: MipmapStrategy | None = None  # Defaults to `auto`.
    alpha_cutoff_bias: Annotated[float, Field(ge=-1, le=1)] | None = None  # The alpha bias for cutout textures.  Positive values make the texture more opaque at distance. Negative values make the texture more transparent at distance.  Defaults to 0.0


class PaletteStruct(GeneratedModel):
    base_palette: PaletteRef


class TextureMeta(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'texture_meta'

    animation: AnimationStruct | None = None
    gui: GuiStruct | None = None
    villager: VillagerStruct | None = None  # Only available for villager textures.
    texture: TextureStruct | None = None
    palette: PaletteStruct | None = None  # Required for armor trim textures.
