# Generated from symbols.json for ::java::world::item::goat_horn::GoatHorn
from dataclasses import dataclass
from generated_symbols.world.item.ItemBase import ItemBase


@dataclass(kw_only=True)
class GoatHorn(ItemBase):
    instrument: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::goat_horn::GoatHorn": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "key": "instrument",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "instrument"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

