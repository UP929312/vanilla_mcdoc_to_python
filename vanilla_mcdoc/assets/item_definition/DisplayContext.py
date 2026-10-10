"""
Generated from symbols.json for ::java::assets::item_definition::DisplayContext
Local link to file: vanilla_mcdoc/assets/item_definition/DisplayContext.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.assets.model.ItemDisplayContext import ItemDisplayContext


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
