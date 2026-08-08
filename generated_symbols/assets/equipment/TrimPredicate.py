# Generated from symbols.json for ::java::assets::equipment::TrimPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class TrimPredicate:
    pattern: str | None = None
    material: str | None = None


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

