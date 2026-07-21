# Generated from symbols.json for ::java::world::item::book::WrittenBook
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable
    from generated_symbols.world.component.item.BookGeneration import BookGeneration


@dataclass(kw_only=True)
class WrittenBook(ItemBase):
    resolved: bool | None = None  # Whether the dynamic content on the pages has been resolved.
    pages: list[Filterable[str]] | None = None  # Pages of the book as JSON text components.
    generation: BookGeneration | None = None  # Generation of the book. 0 = original, 1 = copy of original, 2 = copy of copy, 3 = tattered.
    author: str | None = None
    title: Filterable[str] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::book::WrittenBook": {
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
                "desc": "Whether the dynamic content on the pages has been resolved.",
                "key": "resolved",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Pages of the book as JSON text components.",
                "key": "pages",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::util::Filterable"
                        },
                        "typeArgs": [
                            {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "text_component"
                                    }
                                ]
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Generation of the book. 0 = original, 1 = copy of original, 2 = copy of copy, 3 = tattered.",
                "key": "generation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::BookGeneration"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "author",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "title",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::Filterable"
                    },
                    "typeArgs": [
                        {
                            "kind": "string"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

