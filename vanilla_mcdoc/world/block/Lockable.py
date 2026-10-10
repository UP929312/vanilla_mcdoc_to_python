"""
Generated from symbols.json for ::java::world::block::Lockable
Local link to file: vanilla_mcdoc/world/block/Lockable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate


class Lockable(GeneratedModel):
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
