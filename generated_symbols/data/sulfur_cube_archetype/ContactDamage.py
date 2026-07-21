# Generated from symbols.json for ::java::data::sulfur_cube_archetype::ContactDamage
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider


@dataclass(kw_only=True)
class ContactDamage:
    damage_type: str
    amount: FloatProvider[Annotated[float, 'Range | Min `0` and above | inclusive']] | Annotated[float, 'Range | Min `0` and above | inclusive']
    attribute_to_source: bool  # Whether the damage is attributed to the sulfur cube.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::sulfur_cube_archetype::ContactDamage": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "damage_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "damage_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "amount",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::FloatProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the damage is attributed to the sulfur cube.",
                "key": "attribute_to_source",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

