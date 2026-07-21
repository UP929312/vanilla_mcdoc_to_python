# Generated from symbols.json for ::java::assets::item_definition::SelectCase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel


T = TypeVar('T')

@dataclass(kw_only=True)
class SelectCase(Generic[T]):
    when: T | list[T]
    model: ItemModel


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::SelectCase": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "when",
                    "type": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::assets::item_definition::T"
                            },
                            {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::assets::item_definition::T"
                                }
                            }
                        ]
                    }
                },
                {
                    "kind": "pair",
                    "key": "model",
                    "type": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::ItemModel"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::assets::item_definition::T"
            }
        ]
    }
}

