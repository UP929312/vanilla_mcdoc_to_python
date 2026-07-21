# Generated from symbols.json for ::java::world::entity::minecart::ContainerMinecart
from dataclasses import dataclass


@dataclass(kw_only=True)
class ContainerMinecart:
    LootTable: str | None = None  # Loot table that will populate this minecart.
    LootTableSeed: int | None = None  # Seed of the loot table.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::ContainerMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Loot table that will populate this minecart.",
                "key": "LootTable",
                "type": {
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
                                            "value": "loot_table"
                                        }
                                    },
                                    "empty": {
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
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Seed of the loot table.",
                "key": "LootTableSeed",
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

