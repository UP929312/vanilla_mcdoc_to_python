"""
Generated from symbols.json for ::java::data::advancement::trigger::BeeNestDestroyedTrigger
Local link to file: generated_symbols/data/advancement/trigger/BeeNestDestroyedTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from generated_symbols.util.registry_ref.BlockListRef import BlockListRef


type StateStructBlockStatesNone = dict[str, str]


@dataclass(kw_only=True)
class BeeNestDestroyedTriggerTypeArg(PlayerConditions):
    blocks: BlockListRef | None = None
    state: StateStructBlockStatesNone | None = None
    num_bees_inside: int | None = None  # Number of bees that were inside the bee nest/beehive before it was broken.
    item: ItemPredicate | None = None  # Item used to break the block.


BeeNestDestroyedTrigger = AllOptional[BeeNestDestroyedTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::BeeNestDestroyedTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
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
                        "key": "block",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "block"
                                        }
                                    }
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
                                        "value": "26.3"
                                    }
                                }
                            }
                        ],
                        "key": "blocks",
                        "type": {
                            "kind": "reference",
                            "path": "::java::util::registry_ref::BlockListRef"
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
                                        "value": "26.3"
                                    }
                                }
                            }
                        ],
                        "key": "state",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "blocks"
                                    ]
                                }
                            ],
                            "registry": "mcdoc:block_states"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Number of bees that were inside the bee nest/beehive before it was broken.",
                        "key": "num_bees_inside",
                        "type": {
                            "kind": "int"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Item used to break the block.",
                        "key": "item",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::ItemPredicate"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

