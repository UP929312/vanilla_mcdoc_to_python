"""
Generated from symbols.json for ::java::assets::item_definition::HasComponent
Local link to file: generated_symbols/assets/item_definition/HasComponent.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class HasComponent:
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

