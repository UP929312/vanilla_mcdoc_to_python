# Generated from symbols.json for ::java::data::util::FixedScoreProvider
from dataclasses import dataclass


@dataclass(kw_only=True)
class FixedScoreProvider:
    name: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::FixedScoreProvider": {
        "kind": "struct",
        "fields": [
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

