# Generated from symbols.json for ::java::assets::equipment::Layers
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.equipment.Layer import Layer
    from generated_symbols.assets.equipment.WingsLayer import WingsLayer


@dataclass(kw_only=True)
class Layers:
    humanoid: list[Layer[str]] | None = None
    humanoid_leggings: list[Layer[str]] | None = None
    humanoid_baby: list[Layer[str]] | None = None
    wings: list[WingsLayer[str]] | None = None
    wolf_body: list[Layer[str]] | None = None
    horse_body: list[Layer[str]] | None = None
    llama_body: list[Layer[str]] | None = None
    happy_ghast_body: list[Layer[str]] | None = None
    nautilus_saddle: list[Layer[str]] | None = None
    nautilus_body: list[Layer[str]] | None = None
    pig_saddle: list[Layer[str]] | None = None
    strider_saddle: list[Layer[str]] | None = None
    camel_husk_saddle: list[Layer[str]] | None = None
    camel_saddle: list[Layer[str]] | None = None
    horse_saddle: list[Layer[str]] | None = None
    donkey_saddle: list[Layer[str]] | None = None
    mule_saddle: list[Layer[str]] | None = None
    zombie_horse_saddle: list[Layer[str]] | None = None
    skeleton_horse_saddle: list[Layer[str]] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::Layers": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "humanoid",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/humanoid/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "humanoid_leggings",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/humanoid_leggings/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "humanoid_baby",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/humanoid_baby/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "wings",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::WingsLayer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/wings/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "wolf_body",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/wolf_body/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "horse_body",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/horse_body/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "llama_body",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/llama_body/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
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
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "key": "happy_ghast_body",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/happy_ghast_body/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
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
                "key": "nautilus_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/nautilus_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
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
                "key": "nautilus_body",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/nautilus_body/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "pig_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/pig_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "strider_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/strider_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
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
                "key": "camel_husk_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/camel_husk_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "camel_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/camel_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "horse_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/horse_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "donkey_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/donkey_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "mule_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/mule_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "zombie_horse_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/zombie_horse_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "skeleton_horse_saddle",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
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
                                                        "value": "texture"
                                                    }
                                                },
                                                "path": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "entity/equipment/skeleton_horse_saddle/"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

