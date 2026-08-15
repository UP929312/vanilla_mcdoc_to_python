"""
Generated from symbols.json for ::java::util::text::ShowEntity
Local link to file: generated_symbols/util/text/ShowEntity.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class ShowEntity:
    id: Annotated[str, IdSpec(registry='entity_type')]
    uuid: tuple[int, int, int, int] | str
    name: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ShowEntity": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "deprecated",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    },
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
                "key": "value",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "string"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "type",
                            "type": {
                                "kind": "string"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "id",
                            "type": {
                                "kind": "string"
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
                                "value": "1.16"
                            }
                        }
                    },
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
                "key": "contents",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "type",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "entity_type"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "id",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "list",
                                        "item": {
                                            "kind": "int"
                                        },
                                        "lengthRange": {
                                            "kind": 0,
                                            "min": 4,
                                            "max": 4
                                        },
                                        "attributes": [
                                            {
                                                "name": "canonical"
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "string"
                                    }
                                ],
                                "attributes": [
                                    {
                                        "name": "uuid"
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::text::Text"
                            },
                            "optional": True
                        }
                    ]
                },
                "optional": True
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
                            "key": "id",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "entity_type"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "uuid",
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "list",
                                        "item": {
                                            "kind": "int"
                                        },
                                        "lengthRange": {
                                            "kind": 0,
                                            "min": 4,
                                            "max": 4
                                        },
                                        "attributes": [
                                            {
                                                "name": "canonical"
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "string"
                                    }
                                ],
                                "attributes": [
                                    {
                                        "name": "uuid"
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "reference",
                                "path": "::java::util::text::Text"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

