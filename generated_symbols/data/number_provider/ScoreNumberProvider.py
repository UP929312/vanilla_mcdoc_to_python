# Generated from symbols.json for ::java::data::number_provider::ScoreNumberProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.ScoreProvider import ScoreProvider


@dataclass(kw_only=True)
class ScoreNumberProvider:
    target: ScoreProvider
    score: str
    scale: float | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::ScoreNumberProvider": {
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

