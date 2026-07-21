# Generated from symbols.json for ::java::assets::item_definition::ComponentStrings
from dataclasses import dataclass
from typing import Any
from generated_symbols.assets.item_definition.SelectCases import SelectCases


@dataclass(kw_only=True)
class ComponentStrings(SelectCases[Any]):
    component: str  # The component type to check the values of. If the selected value comes from a registry that the client doesn't have access to, the entry will be silently ignored.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ComponentStrings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The component type to check the values of.\nIf the selected value comes from a registry that the client doesn't have access to,\nthe entry will be silently ignored.",
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
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "component"
                                    ]
                                }
                            ],
                            "registry": "minecraft:data_component"
                        }
                    ]
                }
            }
        ]
    }
}

