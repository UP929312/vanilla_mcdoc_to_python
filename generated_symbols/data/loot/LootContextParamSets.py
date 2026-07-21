# Generated from symbols.json for ::java::data::loot::LootContextParamSets
from enum import Enum


class LootContextParamSets(Enum):
    EMPTY = "empty"
    CHEST = "chest"
    COMMAND = "command"
    SELECTOR = "selector"
    FISHING = "fishing"
    ENTITY = "entity"
    GIFT = "gift"
    BARTER = "barter"
    ADVANCEMENTREWARD = "advancement_reward"
    ADVANCEMENTENTITY = "advancement_entity"
    ADVANCEMENTLOCATION = "advancement_location"
    GENERIC = "generic"
    BLOCK = "block"
    BLOCKUSE = "block_use"
    EQUIPMENT = "equipment"
    ARCHAEOLOGY = "archaeology"
    VAULT = "vault"
    SHEARING = "shearing"
    ENCHANTEDDAMAGE = "enchanted_damage"
    ENCHANTEDITEM = "enchanted_item"
    ENCHANTEDLOCATION = "enchanted_location"
    ENCHANTEDENTITY = "enchanted_entity"
    HITBLOCK = "hit_block"
    BLOCKINTERACT = "block_interact"
    ENTITYINTERACT = "entity_interact"
    VILLAGERTRADE = "villager_trade"
    COMMANDSLOTSOURCE = "command_slot_source"
    CONTAINERPROCESS = "container_process"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootContextParamSets": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Empty",
                "value": "empty"
            },
            {
                "identifier": "Chest",
                "value": "chest"
            },
            {
                "identifier": "Command",
                "value": "command"
            },
            {
                "identifier": "Selector",
                "value": "selector"
            },
            {
                "identifier": "Fishing",
                "value": "fishing"
            },
            {
                "identifier": "Entity",
                "value": "entity"
            },
            {
                "identifier": "Gift",
                "value": "gift"
            },
            {
                "identifier": "Barter",
                "value": "barter"
            },
            {
                "identifier": "AdvancementReward",
                "value": "advancement_reward"
            },
            {
                "identifier": "AdvancementEntity",
                "value": "advancement_entity"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "identifier": "AdvancementLocation",
                "value": "advancement_location"
            },
            {
                "identifier": "Generic",
                "value": "generic"
            },
            {
                "identifier": "Block",
                "value": "block"
            },
            {
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
                "identifier": "BlockUse",
                "value": "block_use"
            },
            {
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
                "identifier": "Equipment",
                "value": "equipment"
            },
            {
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
                "identifier": "Archaeology",
                "value": "archaeology"
            },
            {
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
                "identifier": "Vault",
                "value": "vault"
            },
            {
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
                "identifier": "Shearing",
                "value": "shearing"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "EnchantedDamage",
                "value": "enchanted_damage"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "EnchantedItem",
                "value": "enchanted_item"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "EnchantedLocation",
                "value": "enchanted_location"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "EnchantedEntity",
                "value": "enchanted_entity"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "HitBlock",
                "value": "hit_block"
            },
            {
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
                ],
                "identifier": "BlockInteract",
                "value": "block_interact"
            },
            {
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
                ],
                "identifier": "EntityInteract",
                "value": "entity_interact"
            },
            {
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
                ],
                "identifier": "VillagerTrade",
                "value": "villager_trade"
            },
            {
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
                "identifier": "CommandSlotSource",
                "value": "command_slot_source"
            },
            {
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
                "identifier": "ContainerProcess",
                "value": "container_process"
            }
        ]
    }
}

