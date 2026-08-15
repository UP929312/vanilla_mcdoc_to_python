"""
Generated from symbols.json for ::java::assets::item_definition::ContextDimension
Local link to file: generated_symbols/assets/item_definition/ContextDimension.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.assets.item_definition.SelectCases import SelectCases
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
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

