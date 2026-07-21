# Generated from symbols.json for ::java::data::variants::BiomeCheck
from dataclasses import dataclass


@dataclass(kw_only=True)
class BiomeCheck:
    biomes: str | list[str]  # Checks if the entity is spawning in specific biomes.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::BiomeCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Checks if the entity is spawning in specific biomes.",
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
            }
        ]
    }
}

