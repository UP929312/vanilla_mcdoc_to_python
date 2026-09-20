"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::ContactDamage
Local link to file: generated_symbols/data/sulfur_cube_archetype/ContactDamage.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.FloatProvider import FloatProvider


class ContactDamage(GeneratedModel):
    damage_type: Annotated[str, IdSpec(registry='damage_type')]
    amount: FloatProvider[Annotated[float, Field(ge=0)]] | Annotated[float, Field(ge=0)]
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

