# Generated from symbols.json for ::java::data::loot::function::BannerPatternLayer
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.DyeColor import DyeColor


@dataclass(kw_only=True)
class BannerPatternLayer:
    pattern: str
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

