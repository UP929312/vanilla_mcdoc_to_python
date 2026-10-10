"""
Generated from symbols.json for ::java::assets::equipment::TrimPredicate
Local link to file: vanilla_mcdoc/assets/equipment/TrimPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TrimPredicate(GeneratedModel):
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | None = None
    material: Annotated[str, IdSpec(registry='trim_material')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::TrimPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pattern",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "trim_pattern"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "material",
                "type": {
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
                },
                "optional": True
            }
        ]
    }
}
