"""
Generated from symbols.json for ::java::data::util::ScoreProvider
Local link to file: generated_symbols/data/util/ScoreProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.util.ContextScoreProvider import ContextScoreProvider
from generated_symbols.data.util.FixedScoreProvider import FixedScoreProvider

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget


@dataclass(kw_only=True)
class ScoreProviderStructContext(ContextScoreProvider):
    type: Literal['minecraft:context']


@dataclass(kw_only=True)
class ScoreProviderStructFixed(FixedScoreProvider):
    type: Literal['minecraft:fixed']


type ScoreProviderStruct = ScoreProviderStructContext | ScoreProviderStructFixed

type ScoreProvider = EntityTarget | ScoreProviderStruct


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

