"""
Generated from symbols.json for ::java::world::block::banner::BannerPatternLayer
Local link to file: vanilla_mcdoc/world/block/banner/BannerPatternLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.banner_pattern.BannerPattern import BannerPattern
    from vanilla_mcdoc.util.DyeColor import DyeColor


class BannerPatternLayer(GeneratedModel):
    color: DyeColor  # The dye color of the pattern.
    pattern: Annotated[str, IdSpec(registry='banner_pattern')] | BannerPattern  # The banner pattern.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::banner::BannerPatternLayer": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "The dye color of the pattern.",
                        "key": "Color",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::DyeColorInt"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "The pattern ID.",
                        "key": "Pattern",
                        "type": {
                            "kind": "reference",
                            "path": "::java::world::block::banner::BannerPatternType"
                        },
                        "optional": True
                    }
                ],
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "The dye color of the pattern.",
                        "key": "color",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::DyeColor"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "The banner pattern.",
                        "key": "pattern",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "string",
                                    "attributes": [
                                        {
                                            "name": "id",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "banner_pattern"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::data::variants::banner_pattern::BannerPattern"
                                }
                            ]
                        }
                    }
                ],
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ]
            }
        ]
    }
}
