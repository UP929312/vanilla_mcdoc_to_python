"""
Generated from symbols.json for ::java::util::text::ScoreHolder
Local link to file: generated_symbols/util/text/ScoreHolder.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class ScoreHolder(GeneratedModel):
    objective: str
    name: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ScoreHolder": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "objective",
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
                "key": "name",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "score_holder"
                        }
                    ]
                }
            }
        ]
    }
}

