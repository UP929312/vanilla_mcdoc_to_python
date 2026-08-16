"""
Generated from symbols.json for ::java::data::worldgen::feature::EndPodiumConfig
Local link to file: generated_symbols/data/worldgen/feature/EndPodiumConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar


@dataclass(kw_only=True)
class EndPodiumConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

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

