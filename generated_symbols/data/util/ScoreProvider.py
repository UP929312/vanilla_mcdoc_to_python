"""
Generated from symbols.json for ::java::data::util::ScoreProvider
Local link to file: generated_symbols/data/util/ScoreProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from generated_symbols.data.util.ContextScoreProvider import ContextScoreProvider
from generated_symbols.data.util.FixedScoreProvider import FixedScoreProvider

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget


class ScoreProviderStructContext(ContextScoreProvider):
    type: Literal['minecraft:context', 'context'] = 'minecraft:context'


class ScoreProviderStructFixed(FixedScoreProvider):
    type: Literal['minecraft:fixed', 'fixed'] = 'minecraft:fixed'


type ScoreProviderStruct = Annotated[
    ScoreProviderStructContext | ScoreProviderStructFixed,
    Field(discriminator='type'),
]

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

