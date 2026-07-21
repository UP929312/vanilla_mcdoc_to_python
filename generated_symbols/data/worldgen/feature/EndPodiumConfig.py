# Generated from symbols.json for ::java::data::worldgen::feature::EndPodiumConfig
from dataclasses import dataclass


@dataclass(kw_only=True)
class EndPodiumConfig:
    active: bool | None = None  # Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::EndPodiumConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to `False`.",
                "key": "active",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

