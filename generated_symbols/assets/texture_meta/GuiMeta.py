# Generated from symbols.json for ::java::assets::texture_meta::GuiMeta
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.texture_meta.GuiSpriteScaling import GuiSpriteScaling


@dataclass(kw_only=True)
class GuiMeta:
    scaling: GuiSpriteScaling | None = None  # Configures how the GUI texture should be scaled. Defaults to `stretch`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::GuiMeta": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Configures how the GUI texture should be scaled. Defaults to `stretch`.",
                "key": "scaling",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::texture_meta::GuiSpriteScaling"
                },
                "optional": True
            }
        ]
    }
}

