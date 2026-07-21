# Generated from symbols.json for ::java::data::worldgen::feature::tree::HeightFoliagePlacer
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class HeightFoliagePlacer:
    height: Annotated[int, 'Range | `0`-`16` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::HeightFoliagePlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                }
            }
        ]
    }
}

