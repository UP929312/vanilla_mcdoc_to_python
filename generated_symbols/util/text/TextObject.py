# Generated from symbols.json for ::java::util::text::TextObject
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any
from generated_symbols.util.text.ObjectTextConfig import ObjectTextConfig
from generated_symbols.util.text.TextBase import TextBase
from generated_symbols.util.text.TextNbtBase import TextNbtBase

if TYPE_CHECKING:
    from generated_symbols.util.avatar.Profile import Profile
    from generated_symbols.util.text.Keybind import Keybind
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class TextObjectStruct1(TextBase):
    text: str
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct2(TextBase):
    translate: str
    fallback: str | None = None
    with_: Annotated[list[Text], 'Length = 1 (inclusive) and above'] | None = None
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct3(TextBase):
    score: Any
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct4(TextBase):
    selector: str
    separator: Text | None = None
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct5(TextBase):
    keybind: Keybind
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct6(TextNbtBase):
    block: str
    nbt: str
    source: str | None = None
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct7(TextNbtBase):
    entity: str
    nbt: str
    source: str | None = None
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct8(TextNbtBase):
    storage: str
    nbt: str
    source: str | None = None
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct9(ObjectTextConfig, TextBase):
    sprite: str
    atlas: str | None = None  # Defaults to `minecraft:blocks`.
    object: str | None = None
    type: str | None = None

@dataclass(kw_only=True)
class TextObjectStruct10(ObjectTextConfig, TextBase):
    player: Profile
    hat: bool | None = None  # Whether the head layer is rendered. Defaults to `true`.
    object: str | None = None
    type: str | None = None

type TextObject = TextObjectStruct1 | TextObjectStruct2 | TextObjectStruct3 | TextObjectStruct4 | TextObjectStruct5 | TextObjectStruct6 | TextObjectStruct7 | TextObjectStruct8 | TextObjectStruct9 | TextObjectStruct10


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::TextObject": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "text",
                        "type": {
                            "kind": "string"
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "text"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "translate",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "translation_key"
                                }
                            ]
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
                                        "value": "1.19.4"
                                    }
                                }
                            }
                        ],
                        "key": "fallback",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "translation_value"
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "with",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::util::text::Text"
                            },
                            "lengthRange": {
                                "kind": 0,
                                "min": 1
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "translatable"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "score",
                        "type": {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": "objective",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "objective"
                                            }
                                        ]
                                    }
                                },
                                {
                                    "kind": "pair",
                                    "key": "name",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "score_holder"
                                            }
                                        ]
                                    }
                                }
                            ]
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "score"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "selector",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "entity"
                                }
                            ]
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
                                        "value": "1.17"
                                    }
                                }
                            }
                        ],
                        "key": "separator",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::Text"
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "selector"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "keybind",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::Keybind"
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "keybind"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "block",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "vector",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "dimension": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "int",
                                                    "value": 3
                                                }
                                            },
                                            "integer": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "boolean",
                                                    "value": True
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
                        "key": "nbt",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "nbt_path",
                                    "value": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "static",
                                                "value": "%fallback"
                                            }
                                        ],
                                        "registry": "minecraft:block"
                                    }
                                }
                            ]
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "source",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "block"
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "nbt"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextNbtBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "entity",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "entity",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "amount": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "multiple"
                                                }
                                            },
                                            "type": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "entities"
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
                        "key": "nbt",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "nbt_path",
                                    "value": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    "entity"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:entity"
                                    }
                                }
                            ]
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "source",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "entity"
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "nbt"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextNbtBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "storage",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "storage"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "nbt",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "nbt_path",
                                    "value": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    "storage"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:storage"
                                    }
                                }
                            ]
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "source",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "storage"
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
                                        "value": "1.20.3"
                                    }
                                }
                            }
                        ],
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "nbt"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextNbtBase"
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Defaults to `minecraft:blocks`.",
                        "key": "atlas",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "atlas"
                                        }
                                    }
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "sprite",
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
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::ObjectTextConfig"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "object",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "atlas"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "object"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
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
                                "value": "1.21.9"
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
                        "key": "player",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::avatar::Profile"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Whether the head layer is rendered. Defaults to `True`.",
                        "key": "hat",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::ObjectTextConfig"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "object",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "player"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "object"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::text::TextBase"
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
                                "value": "1.21.9"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

