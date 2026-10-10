"""
Generated from symbols.json for ::java::data::loot::LootPoolEntryBase
Local link to file: vanilla_mcdoc/data/loot/LootPoolEntryBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifier import ItemModifier
    from vanilla_mcdoc.data.predicate.PredicateRef import PredicateRef


class LootPoolEntryBase(GeneratedModel):
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
