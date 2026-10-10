"""
Generated from symbols.json for ::java::data::advancement::trigger::LootTableTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/LootTableTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.ParitalRequired import ParitalRequired
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.loot.LootTableListRef import LootTableListRef


class LootTableTriggerTypeArg(PlayerConditions):
    loot_tables: LootTableListRef


LootTableTrigger = ParitalRequired[LootTableTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::LootTableTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::ParitalRequired"
        },
        "typeArgs": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::PlayerConditions"
                        }
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
                                        "value": "26.3"
                                    }
                                }
                            }
                        ],
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
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "26.3"
                                    }
                                }
                            }
                        ],
                        "key": "loot_tables",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::loot::LootTableListRef"
                        }
                    }
                ]
            }
        ]
    }
}
