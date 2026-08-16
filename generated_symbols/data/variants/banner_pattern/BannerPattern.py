"""
Generated from symbols.json for ::java::data::variants::banner_pattern::BannerPattern
Local link to file: generated_symbols/data/variants/banner_pattern/BannerPattern.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class BannerPattern:
    __resource_dir__: ClassVar[str] = 'banner_pattern'

    asset_id: Annotated[str, IdSpec(registry='texture', path='entity/banner/')]  # Also resolves to `assets/<namespace>/textures/entity/shield/<name>.png`.
    translation_key: str  # Translation key prefix per dye color (e.g. `block.minecraft.banner.custom.pattern` resolves to `block.minecraft.banner.custom.pattern.<dye color>`).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::banner_pattern::BannerPattern": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Also resolves to `assets/<namespace>/textures/entity/shield/<name>.png`.",
                "key": "asset_id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "texture"
                                        }
                                    },
                                    "path": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity/banner/"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Translation key prefix per dye color (e.g. `block.minecraft.banner.custom.pattern` resolves to `block.minecraft.banner.custom.pattern.<dye color>`).",
                "key": "translation_key",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

