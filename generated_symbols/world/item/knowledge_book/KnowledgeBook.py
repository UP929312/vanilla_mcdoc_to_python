"""
Generated from symbols.json for ::java::world::item::knowledge_book::KnowledgeBook
Local link to file: generated_symbols/world/item/knowledge_book/KnowledgeBook.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.world.item.ItemBase import ItemBase
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class KnowledgeBook(ItemBase):
    Recipes: list[Annotated[str, IdSpec(registry='recipe')]] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::knowledge_book::KnowledgeBook": {
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
                "key": "Recipes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "recipe"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

