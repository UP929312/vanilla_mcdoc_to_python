"""
Generated from symbols.json for ::java::data::loot::condition::KilledByPlayer
Local link to file: vanilla_mcdoc/data/loot/condition/KilledByPlayer.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class KilledByPlayer(GeneratedModel):
    inverse: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::KilledByPlayer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "inverse",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
