# Generated from symbols.json for ::java::data::worldgen::feature::RandomFeatureEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class RandomFeatureEntry:
    chance: Annotated[float, 'Range | `0`-`1` | both inclusive']
    feature: FeatureRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::RandomFeatureEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "chance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            }
        ]
    }
}

