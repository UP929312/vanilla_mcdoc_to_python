"""
Generated from symbols.json for ::java::assets::item_definition::ContextEntityType
Local link to file: generated_symbols/assets/item_definition/ContextEntityType.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.assets.item_definition.SelectCases import SelectCases
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class ContextEntityType(SelectCases[Annotated[str, IdSpec(registry='entity_type')]]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ContextEntityType": {
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
                                            "value": "entity_type"
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

