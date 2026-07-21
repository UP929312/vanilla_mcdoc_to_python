# Generated from symbols.json for ::java::world::item::knowledge_book::KnowledgeBook
from dataclasses import dataclass
from generated_symbols.world.item.ItemBase import ItemBase


@dataclass(kw_only=True)
class KnowledgeBook(ItemBase):
    Recipes: list[str] | None = None


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

