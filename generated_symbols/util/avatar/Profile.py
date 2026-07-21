# Generated from symbols.json for ::java::util::avatar::Profile
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.avatar.PlayerModelType import PlayerModelType
    from generated_symbols.util.avatar.ProfileProperty import ProfileProperty
    from generated_symbols.util.avatar.ProfilePropertyMap import ProfilePropertyMap


@dataclass(kw_only=True)
class ProfileStruct1:
    name: str | None = None  # Username of a player profile. If `id` doesn't exist, this field is used to fetch the current skin of the profile.
    id: tuple[int, int, int, int] | None = None  # UUID of the player profile. If `name` doesn't exist, this field is used to fetch the current skin of the profile.
    properties: Annotated[list[ProfileProperty], 'Length = 0-16 (both inclusive)'] | ProfilePropertyMap | None = None  # Resolved textures hosted on the minecraft CDN.
    texture: str | None = None  # Skin texture override.
    cape: str | None = None  # Cape texture override.
    elytra: str | None = None  # Elytra texture override. If this texture is not present either as override or in player profile, the cape texture is used. If the cape texture is also not present, the default elytra texture is used.
    model: PlayerModelType | None = None  # Model type override.

type Profile = ProfileStruct1 | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::avatar::Profile": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Username of a player profile.",
                        "key": "name",
                        "type": {
                            "kind": "string"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "UUID of the owner. Used to update the other tags when the chunk loads or the holder logs in, in case the owner's name has changed.",
                        "key": "id",
                        "type": {
                            "kind": "int_array",
                            "lengthRange": {
                                "kind": 0,
                                "min": 4,
                                "max": 4
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Resolved textures hosted on the minecraft CDN.",
                        "key": "properties",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "list",
                                    "item": {
                                        "kind": "reference",
                                        "path": "::java::util::avatar::ProfileProperty"
                                    },
                                    "attributes": [
                                        {
                                            "name": "canonical"
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::util::avatar::ProfilePropertyMap"
                                }
                            ]
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
                                "value": "1.21.9"
                            }
                        }
                    },
                    {
                        "name": "canonical"
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Username of a player profile.\nIf `id` doesn't exist, this field is used to fetch the current skin of the profile.",
                        "key": "name",
                        "type": {
                            "kind": "string"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "UUID of the player profile.\nIf `name` doesn't exist, this field is used to fetch the current skin of the profile.",
                        "key": "id",
                        "type": {
                            "kind": "int_array",
                            "lengthRange": {
                                "kind": 0,
                                "min": 4,
                                "max": 4
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Resolved textures hosted on the minecraft CDN.",
                        "key": "properties",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "list",
                                    "item": {
                                        "kind": "reference",
                                        "path": "::java::util::avatar::ProfileProperty"
                                    },
                                    "attributes": [
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.21.11"
                                                }
                                            }
                                        },
                                        {
                                            "name": "canonical"
                                        }
                                    ]
                                },
                                {
                                    "kind": "list",
                                    "item": {
                                        "kind": "reference",
                                        "path": "::java::util::avatar::ProfileProperty"
                                    },
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 0,
                                        "max": 16
                                    },
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
                                        },
                                        {
                                            "name": "canonical"
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::util::avatar::ProfilePropertyMap"
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Skin texture override.",
                        "key": "texture",
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
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Cape texture override.",
                        "key": "cape",
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
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Elytra texture override.\nIf this texture is not present either as override or in player profile, the cape texture is used.\nIf the cape texture is also not present, the default elytra texture is used.",
                        "key": "elytra",
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
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Model type override.",
                        "key": "model",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::avatar::PlayerModelType"
                        },
                        "optional": True
                    }
                ],
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    },
                    {
                        "name": "canonical"
                    }
                ]
            },
            {
                "kind": "string"
            }
        ]
    }
}

