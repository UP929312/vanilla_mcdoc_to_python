# Generated from symbols.json for ::java::world::component::block::ContainerLoot
from dataclasses import dataclass


@dataclass(kw_only=True)
class ContainerLoot:
    loot_table: str
    seed: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::ContainerLoot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "loot_table",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_table"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "seed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

