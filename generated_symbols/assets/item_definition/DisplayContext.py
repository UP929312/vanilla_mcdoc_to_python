# Generated from symbols.json for ::java::assets::item_definition::DisplayContext
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.assets.item_definition.SelectCases import SelectCases

if TYPE_CHECKING:
    from generated_symbols.assets.model.ItemDisplayContext import ItemDisplayContext


@dataclass(kw_only=True)
class DisplayContext(SelectCases[ItemDisplayContext]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::DisplayContext": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::assets::model::ItemDisplayContext"
                        }
                    ]
                }
            }
        ]
    }
}

