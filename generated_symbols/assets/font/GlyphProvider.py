# Generated from symbols.json for ::java::assets::font::GlyphProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.font.FontOption import FontOption
    from generated_symbols.assets.font.GlyphProviderType import GlyphProviderType


@dataclass(kw_only=True)
class GlyphProvider:
    type: GlyphProviderType
    filter: dict[FontOption, bool] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::GlyphProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::font::GlyphProviderType"
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
                    "registry": "minecraft:glyph_provider"
                }
            },
            {
                "kind": "pair",
                "key": "filter",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "reference",
                                "path": "::java::assets::font::FontOption"
                            },
                            "type": {
                                "kind": "boolean"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

