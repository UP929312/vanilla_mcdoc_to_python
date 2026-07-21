# Generated from symbols.json for ::java::data::variants::wolf::WolfVariant
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors

if TYPE_CHECKING:
    from generated_symbols.data.variants.wolf.WolfVariantAssetInfo import WolfVariantAssetInfo


@dataclass(kw_only=True)
class WolfVariant(SpawnPrioritySelectors):
    assets: WolfVariantAssetInfo  # The texture set to use for this wolf variant.
    baby_assets: WolfVariantAssetInfo  # The baby texture set to use for this wolf variant.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::wolf::WolfVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "biomes",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
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
                                                                "value": "worldgen/biome"
                                                            }
                                                        },
                                                        "tags": {
                                                            "kind": "literal",
                                                            "value": {
                                                                "kind": "string",
                                                                "value": "allowed"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "list",
                                        "item": {
                                            "kind": "string",
                                            "attributes": [
                                                {
                                                    "name": "id",
                                                    "value": {
                                                        "kind": "literal",
                                                        "value": {
                                                            "kind": "string",
                                                            "value": "worldgen/biome"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "wild_texture",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "texture"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "tame_texture",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "texture"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "angry_texture",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "texture"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "The texture set to use for this wolf variant.",
                            "key": "assets",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::variants::wolf::WolfVariantAssetInfo"
                            }
                        },
                        {
                            "kind": "pair",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.1"
                                        }
                                    }
                                }
                            ],
                            "desc": "The baby texture set to use for this wolf variant.",
                            "key": "baby_assets",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::variants::wolf::WolfVariantAssetInfo"
                            }
                        },
                        {
                            "kind": "spread",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::variants::SpawnPrioritySelectors"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

