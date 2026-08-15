"""
Generated from symbols.json for ::java::assets::item_definition::TrimMaterial
Local link to file: generated_symbols/assets/item_definition/TrimMaterial.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.assets.item_definition.SelectCases import SelectCases
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class TrimMaterial(SelectCases[Annotated[str, IdSpec(registry='trim_material')]]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::TrimMaterial": {
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
                                            "value": "trim_material"
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

