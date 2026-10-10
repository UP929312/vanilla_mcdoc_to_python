"""
Generated from symbols.json for ::java::assets::texture_meta::GuiMeta
Local link to file: vanilla_mcdoc/assets/texture_meta/GuiMeta.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.texture_meta.GuiSpriteScaling import GuiSpriteScaling


class GuiMeta(GeneratedModel):
    scaling: GuiSpriteScaling | None = None  # Configures how the GUI texture should be scaled. Defaults to `stretch`.
