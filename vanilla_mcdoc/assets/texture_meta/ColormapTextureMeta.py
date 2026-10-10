"""
Generated from symbols.json for ::java::assets::texture_meta::ColormapTextureMeta
Local link to file: vanilla_mcdoc/assets/texture_meta/ColormapTextureMeta.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.texture_meta.MipmapStrategy import MipmapStrategy


class ColormapTextureMeta(GeneratedModel):
    blur: bool | None = None  # Causes the texture to blur when viewed from close up. Defaults to false.
    clamp: bool | None = None  # Causes the texture to stretch instead of tiling in cases where it otherwise would, such as on the shadow. Defaults to false.
    mipmap_strategy: MipmapStrategy | None = None  # Defaults to `auto`.
    alpha_cutoff_bias: Annotated[float, Field(ge=-1, le=1)] | None = None  # The alpha bias for cutout textures.  Positive values make the texture more opaque at distance. Negative values make the texture more transparent at distance.  Defaults to 0.0
