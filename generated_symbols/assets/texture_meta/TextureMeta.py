# Generated from symbols.json for ::java::assets::texture_meta::TextureMeta
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class TextureMeta:
    animation: Any | None = None
    gui: Any | None = None
    villager: Any | None = None  # Only available for villager textures.
    texture: Any | None = None
    palette: Any | None = None  # Required for armor trim textures.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::TextureMeta": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "animation",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "If True, additional frames will be generated between frames with a frame time greater than 1 between them. Defaults to False.",
                            "key": "interpolate",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The width of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.",
                            "key": "width",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "The height of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.",
                            "key": "height",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Sets the default time for each frame in increments of one game tick. Defaults to 1.",
                            "key": "frametime",
                            "type": {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 1
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Defaults to displaying all the frames from top to bottom.",
                            "key": "frames",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "union",
                                    "members": [
                                        {
                                            "kind": "struct",
                                            "fields": [
                                                {
                                                    "kind": "pair",
                                                    "desc": "A number corresponding to position of a frame from the top, with the top frame being 0.",
                                                    "key": "index",
                                                    "type": {
                                                        "kind": "int",
                                                        "valueRange": {
                                                            "kind": 0,
                                                            "min": 0
                                                        }
                                                    }
                                                },
                                                {
                                                    "kind": "pair",
                                                    "desc": "The time in ticks to show this frame, overriding `frametime` above.",
                                                    "key": "time",
                                                    "type": {
                                                        "kind": "int",
                                                        "valueRange": {
                                                            "kind": 0,
                                                            "min": 1
                                                        }
                                                    },
                                                    "optional": True
                                                }
                                            ]
                                        },
                                        {
                                            "kind": "int",
                                            "valueRange": {
                                                "kind": 0,
                                                "min": 0
                                            }
                                        }
                                    ]
                                }
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
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
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "key": "gui",
                "type": {
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Only available for villager textures.",
                "key": "villager",
                "type": {
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "texture",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "Causes the texture to blur when viewed from close up. Defaults to False.",
                            "key": "blur",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "desc": "Causes the texture to stretch instead of tiling in cases where it otherwise would, such as on the shadow. Defaults to False.",
                            "key": "clamp",
                            "type": {
                                "kind": "boolean"
                            },
                            "optional": True
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
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ],
                            "desc": "Defaults to `auto`.",
                            "key": "mipmap_strategy",
                            "type": {
                                "kind": "reference",
                                "path": "::java::assets::texture_meta::MipmapStrategy"
                            },
                            "optional": True
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
                                            "value": "1.21.11"
                                        }
                                    }
                                }
                            ],
                            "desc": "The alpha bias for cutout textures. \\\nPositive values make the texture more opaque at distance.\nNegative values make the texture more transparent at distance. \\\nDefaults to 0.0",
                            "key": "alpha_cutoff_bias",
                            "type": {
                                "kind": "float",
                                "valueRange": {
                                    "kind": 0,
                                    "min": -1,
                                    "max": 1
                                }
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "desc": "Required for armor trim textures.",
                "key": "palette",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "base_palette",
                            "type": {
                                "kind": "reference",
                                "path": "::java::assets::atlas::PaletteRef"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

