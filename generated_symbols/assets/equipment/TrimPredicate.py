"""
Generated from symbols.json for ::java::assets::equipment::TrimPredicate
Local link to file: generated_symbols/assets/equipment/TrimPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class TrimPredicate:
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

