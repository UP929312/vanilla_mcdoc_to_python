# Generated from symbols.json for ::java::data::advancement::trigger::BeeNestDestroyed
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.util.registry_ref.BlockListRef import BlockListRef


@dataclass(kw_only=True)
class BeeNestDestroyed(TriggerBase):
    blocks: BlockListRef | None = None
    state: Any | None = None
    num_bees_inside: int | None = None  # Number of bees that were inside the bee nest/beehive before it was broken.
    item: ItemPredicate | None = None  # Item used to break the block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::BeeNestDestroyed": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
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
}

