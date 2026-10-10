"""
Generated from symbols.json for ::java::assets::item_definition::HasComponent
Local link to file: vanilla_mcdoc/assets/item_definition/HasComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class HasComponent(GeneratedModel):
    component: Annotated[str, IdSpec(registry='data_component_type')]
    ignore_default: bool | None = None  # Whether the default components should be handled as "no component". Defaults to false.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::HasComponent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "component",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "data_component_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the default components should be handled as \"no component\". Defaults to False.",
                "key": "ignore_default",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
