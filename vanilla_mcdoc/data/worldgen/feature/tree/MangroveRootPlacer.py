"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::MangroveRootPlacer
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/MangroveRootPlacer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.tree.MangroveRootPlacement import MangroveRootPlacement


class MangroveRootPlacer(GeneratedModel):
    mangrove_root_placement: MangroveRootPlacement


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::MangroveRootPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "mangrove_root_placement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::tree::MangroveRootPlacement"
                }
            }
        ]
    }
}
