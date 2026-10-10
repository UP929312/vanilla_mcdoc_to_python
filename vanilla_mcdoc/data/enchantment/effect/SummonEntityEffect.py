"""
Generated from symbols.json for ::java::data::enchantment::effect::SummonEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/SummonEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class SummonEntityEffect(GeneratedModel):
    entity: Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]]  # If multiple entity types are specified, a random entity type is selected.
    join_team: bool | None = None  # Whether the summoned entity should join the team of the owner of the Enchanted Item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::SummonEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If multiple entity types are specified, a random entity type is selected.",
                "key": "entity",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "entity_type"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
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
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the summoned entity should join the team of the owner of the Enchanted Item.",
                "key": "join_team",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
