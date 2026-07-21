# Generated from symbols.json for ::java::assets::texture_meta::VillagerTextureMeta
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.texture_meta.VillagerHatType import VillagerHatType


@dataclass(kw_only=True)
class VillagerTextureMeta:
    hat: VillagerHatType | None = None  # Determines whether the villager's 'profession' hat layer should allow the 'type' hat layer to render or not.  Defaults to `none`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::VillagerTextureMeta": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Determines whether the villager's 'profession' hat layer should allow the 'type' hat layer to render or not. \\\nDefaults to `none`.",
                "key": "hat",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::texture_meta::VillagerHatType"
                },
                "optional": True
            }
        ]
    }
}

