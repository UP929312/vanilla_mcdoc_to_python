"""
Generated from symbols.json for ::java::util::particle::ItemParticle
Local link to file: generated_symbols/util/particle/ItemParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


class ItemParticle(GeneratedModel):
    item: ItemStackTemplate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::ItemParticle": {
        "kind": "struct",
        "fields": [
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
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
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
                "key": "item",
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
                                            "value": "26.1"
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
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::item::SingleItem",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.1"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::item::ItemStackTemplate",
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
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

