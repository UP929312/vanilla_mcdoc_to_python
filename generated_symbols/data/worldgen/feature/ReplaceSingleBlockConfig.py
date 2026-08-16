"""
Generated from symbols.json for ::java::data::worldgen::feature::ReplaceSingleBlockConfig
Local link to file: generated_symbols/data/worldgen/feature/ReplaceSingleBlockConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.TargetBlock import TargetBlock


@dataclass(kw_only=True)
class ReplaceSingleBlockConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    targets: list[TargetBlock]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ReplaceSingleBlockConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "targets",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::TargetBlock"
                    }
                }
            }
        ]
    }
}

