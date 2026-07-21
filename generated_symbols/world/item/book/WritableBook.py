# Generated from symbols.json for ::java::world::item::book::WritableBook
from dataclasses import dataclass
from generated_symbols.world.item.ItemBase import ItemBase


@dataclass(kw_only=True)
class WritableBook(ItemBase):
    pages: list[str] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::book::WritableBook": {
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
                "key": "pages",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string"
                    }
                },
                "optional": True
            }
        ]
    }
}

