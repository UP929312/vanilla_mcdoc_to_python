# Generated from symbols.json for ::java::data::loot::condition::WeatherCheck
from dataclasses import dataclass


@dataclass(kw_only=True)
class WeatherCheck:
    raining: bool | None = None
    thundering: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::WeatherCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "raining",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "thundering",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

