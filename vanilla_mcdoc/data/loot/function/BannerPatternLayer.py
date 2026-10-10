"""
Generated from symbols.json for ::java::data::loot::function::BannerPatternLayer
Local link to file: vanilla_mcdoc/data/loot/function/BannerPatternLayer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.DyeColor import DyeColor


class BannerPatternLayer(GeneratedModel):
    pattern: Annotated[str, IdSpec(registry='banner_pattern')]
    color: DyeColor


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::BannerPatternLayer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pattern",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::function::BannerPattern",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.4"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.4"
                                        }
                                    }
                                },
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
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::DyeColor"
                }
            }
        ]
    }
}
