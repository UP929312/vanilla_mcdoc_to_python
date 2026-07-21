# Generated from symbols.json for ::java::util::text::ScoreHolder
from dataclasses import dataclass


@dataclass(kw_only=True)
class ScoreHolder:
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

