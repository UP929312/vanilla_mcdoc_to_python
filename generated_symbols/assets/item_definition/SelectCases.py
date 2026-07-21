# Generated from symbols.json for ::java::assets::item_definition::SelectCases
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.SelectCase import SelectCase


T = TypeVar('T')

@dataclass(kw_only=True)
class SelectCases(Generic[T]):
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

