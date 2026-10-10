"""
Generated from symbols.json for ::java::data::worldgen::feature::EndPodiumConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/EndPodiumConfig.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from vanilla_mcdoc.base import GeneratedModel


class EndPodiumConfig(GeneratedModel):
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
