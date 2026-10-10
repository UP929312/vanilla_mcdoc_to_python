"""
Generated from symbols.json for ::java::world::item::SingleItemOfComponent
Local link to file: vanilla_mcdoc/world/item/SingleItemOfComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


T = TypeVar('T')


class SingleItemOfComponent(GeneratedModel, Generic[T]):
    id: Annotated[str, IdSpec(registry='item', exclude=('air',))]  # ID of the item.
    components: T | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::SingleItemOfComponent": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "desc": "ID of the item.",
                    "key": "id",
                    "type": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "string",
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
                                    },
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "item"
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
                                                "value": "1.20.5"
                                            }
                                        }
                                    },
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "tree",
                                            "values": {
                                                "registry": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "item"
                                                    }
                                                },
                                                "exclude": {
                                                    "kind": "tree",
                                                    "values": {
                                                        "0": {
                                                            "kind": "literal",
                                                            "value": {
                                                                "kind": "string",
                                                                "value": "air"
                                                            }
                                                        }
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
                {
                    "kind": "pair",
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
                    ],
                    "key": "components",
                    "type": {
                        "kind": "reference",
                        "path": "::java::world::item::T"
                    },
                    "optional": True
                },
                {
                    "kind": "pair",
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
                    ],
                    "key": "tag",
                    "type": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "dynamic",
                                "accessor": [
                                    "id"
                                ]
                            }
                        ],
                        "registry": "minecraft:item"
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::world::item::T"
            }
        ]
    }
}
