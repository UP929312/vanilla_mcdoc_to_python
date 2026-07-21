# Generated from symbols.json for ::java::data::loot::LootPoolEntryBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.item_modifier.ItemModifier import ItemModifier
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


@dataclass(kw_only=True)
class LootPoolEntryBase:
    modifier: ItemModifier | None = None
    condition: PredicateRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootPoolEntryBase": {
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "conditions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::LootCondition"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
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
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "modifier",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::item_modifier::ItemModifier"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "condition",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::predicate::PredicateRef"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

