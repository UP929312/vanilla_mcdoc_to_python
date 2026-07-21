# Generated from symbols.json for ::java::data::loot::condition::EntityScores
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.util.IntRange import IntRange


@dataclass(kw_only=True)
class EntityScores:
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
                                        "path": "::java::data::util::IntRange",
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

