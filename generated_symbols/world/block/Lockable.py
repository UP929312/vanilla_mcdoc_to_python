# Generated from symbols.json for ::java::world::block::Lockable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate


@dataclass(kw_only=True)
class Lockable:
    lock: ItemPredicate | None = None  # Item predicate testing the item that a player has to be holding to open this container.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::Lockable": {
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Name of the item that a player has to be holding to open this container.\nSource is flattened to plain text and has formatting removed before the check.",
                "key": "Lock",
                "type": {
                    "kind": "string"
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Item predicate testing the item that a player has to be holding to open this container.",
                "key": "lock",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::ItemPredicate"
                },
                "optional": True
            }
        ]
    }
}

