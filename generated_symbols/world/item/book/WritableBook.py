"""
Generated from symbols.json for ::java::world::item::book::WritableBook
Local link to file: generated_symbols/world/item/book/WritableBook.py
"""
# ~~~ CODE ~~~
from generated_symbols.world.item.ItemBase import ItemBase


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

