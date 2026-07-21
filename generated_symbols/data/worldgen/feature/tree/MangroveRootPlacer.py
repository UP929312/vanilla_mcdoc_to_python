# Generated from symbols.json for ::java::data::worldgen::feature::tree::MangroveRootPlacer
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.tree.MangroveRootPlacement import MangroveRootPlacement


@dataclass(kw_only=True)
class MangroveRootPlacer:
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

