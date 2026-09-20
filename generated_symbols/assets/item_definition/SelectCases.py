"""
Generated from symbols.json for ::java::assets::item_definition::SelectCases
Local link to file: generated_symbols/assets/item_definition/SelectCases.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.SelectCase import SelectCase


T = TypeVar('T')

class SelectCases(GeneratedModel, Generic[T]):
    cases: list[SelectCase[T]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::SelectCases": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "cases",
                    "type": {
                        "kind": "list",
                        "item": {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::assets::item_definition::SelectCase"
                            },
                            "typeArgs": [
                                {
                                    "kind": "reference",
                                    "path": "::java::assets::item_definition::T"
                                }
                            ]
                        }
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

