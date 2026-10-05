"""
Generated from symbols.json for ::java::data::number_provider::legacy::ScoreNumberProvider
Local link to file: generated_symbols/data/number_provider/legacy/ScoreNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.ScoreProvider import ScoreProvider


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

