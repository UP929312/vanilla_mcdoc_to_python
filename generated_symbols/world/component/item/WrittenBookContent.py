# Generated from symbols.json for ::java::world::component::item::WrittenBookContent
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.component.item.BookGeneration import BookGeneration


@dataclass(kw_only=True)
class WrittenBookContent:
    title: Filterable[Annotated[str, 'Length = up to 32 (inclusive)']]
    author: str
    pages: list[Filterable[Text]] | None = None
    generation: BookGeneration | None = None  # Number of times this written book has been copied. Defaults to 0. If the value is greater than 1, the book cannot be copied.
    resolved: bool | None = None  # Whether the dynamic content on the pages has been resolved.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::WrittenBookContent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "until",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.21.5"
                                                    }
                                                }
                                            },
                                            {
                                                "name": "text_component"
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::util::text::Text",
                                        "attributes": [
                                            {
                                                "name": "since",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.21.5"
                                                    }
                                                }
                                            }
                                        ]
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
                "key": "title",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::util::Filterable"
                            },
                            "typeArgs": [
                                {
                                    "kind": "string",
                                    "lengthRange": {
                                        "kind": 0,
                                        "max": 32
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "author",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "desc": "Number of times this written book has been copied. Defaults to 0. If the value is greater than 1, the book cannot be copied.",
                "key": "generation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::BookGeneration"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the dynamic content on the pages has been resolved.",
                "key": "resolved",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

