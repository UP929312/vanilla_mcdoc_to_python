"""
Generated from symbols.json for ::java::assets::item_definition::ContextDimension
Local link to file: vanilla_mcdoc/assets/item_definition/ContextDimension.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.minecraft_types import IdSpec


class ContextDimension(SelectCases[Annotated[str, IdSpec(registry='dimension')]]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ContextDimension": {
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
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "dimension"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
