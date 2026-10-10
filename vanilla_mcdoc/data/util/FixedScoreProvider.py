"""
Generated from symbols.json for ::java::data::util::FixedScoreProvider
Local link to file: vanilla_mcdoc/data/util/FixedScoreProvider.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class FixedScoreProvider(GeneratedModel):
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
