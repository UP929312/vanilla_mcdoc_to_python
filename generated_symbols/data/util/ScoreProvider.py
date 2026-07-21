# Generated from symbols.json for ::java::data::util::ScoreProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget


@dataclass(kw_only=True)
class ScoreProviderStruct1:
    type: str

type ScoreProvider = EntityTarget | ScoreProviderStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::ScoreProvider": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::loot::EntityTarget"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_score_provider_type"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:score_provider"
                        }
                    }
                ]
            }
        ]
    }
}

