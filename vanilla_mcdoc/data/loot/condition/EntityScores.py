"""
Generated from symbols.json for ::java::data::loot::condition::EntityScores
Local link to file: vanilla_mcdoc/data/loot/condition/EntityScores.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
    from vanilla_mcdoc.data.loot.IntRange import IntRange


class EntityScores(GeneratedModel):
    entity: EntityTarget
    scores: dict[str, IntRange]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::EntityScores": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::EntityTarget"
                }
            },
            {
                "kind": "pair",
                "key": "scores",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "objective"
                                    }
                                ]
                            },
                            "type": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::util::RandomValueBounds",
                                        "attributes": [
                                            {
                                                "name": "until",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::loot::IntRange",
                                        "attributes": [
                                            {
                                                "name": "since",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "1.17"
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
        ]
    }
}
