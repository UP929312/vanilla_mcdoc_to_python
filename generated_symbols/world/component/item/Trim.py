"""
Generated from symbols.json for ::java::world::component::item::Trim
Local link to file: generated_symbols/world/component/item/Trim.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.trim.TrimMaterial import TrimMaterial
    from generated_symbols.data.trim.TrimPattern import TrimPattern


@dataclass(kw_only=True)
class Trim:
    material: Annotated[str, IdSpec(registry='trim_material')] | TrimMaterial  # The trim material of this item..
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | TrimPattern  # The trim pattern of this item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Trim": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The trim material of this item..",
                "key": "material",
                "type": {
                    "kind": "union",
                    "members": [
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
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::trim::TrimMaterial"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The trim pattern of this item.",
                "key": "pattern",
                "type": {
                    "kind": "union",
                    "members": [
                        {
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
                        {
                            "kind": "reference",
                            "path": "::java::data::trim::TrimPattern"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "show_in_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

