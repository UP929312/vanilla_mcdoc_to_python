# Generated from symbols.json for ::java::world::block::spawner::SpawnPotential
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.WeightedEntry import WeightedEntry
    from generated_symbols.world.block.spawner.SpawnerEntry import SpawnerEntry


type SpawnPotential = WeightedEntry[SpawnerEntry]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::spawner::SpawnPotential": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "Entity",
                        "type": {
                            "kind": "reference",
                            "path": "::java::world::entity::AnyEntity"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Weight for this entry to be chosen.",
                        "key": "Weight",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "int",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0
                                    },
                                    "attributes": [
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.17"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "byte",
                                    "valueRange": {
                                        "kind": 0,
                                        "min": 0
                                    },
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
                                    ]
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
                                "value": "1.18"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "concrete",
                "child": {
                    "kind": "reference",
                    "path": "::java::util::WeightedEntry"
                },
                "typeArgs": [
                    {
                        "kind": "reference",
                        "path": "::java::world::block::spawner::SpawnerEntry"
                    }
                ],
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.18"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

