"""
Generated from symbols.json for ::java::data::number_provider::legacy::ScoreNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/legacy/ScoreNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.ScoreProvider import ScoreProvider


class ScoreNumberProvider(GeneratedModel):
    target: ScoreProvider
    score: str
    scale: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::ScoreNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::ScoreProvider"
                }
            },
            {
                "kind": "pair",
                "key": "score",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "objective"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}
