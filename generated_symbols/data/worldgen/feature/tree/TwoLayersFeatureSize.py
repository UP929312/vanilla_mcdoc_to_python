# Generated from symbols.json for ::java::data::worldgen::feature::tree::TwoLayersFeatureSize
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TwoLayersFeatureSize:
    min_clipped_height: Annotated[float, 'Range | `0`-`80` | both inclusive'] | None = None
    limit: Annotated[int, 'Range | `0`-`81` | both inclusive'] | None = None
    lower_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None
    upper_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TwoLayersFeatureSize": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min_clipped_height",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 80
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "limit",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 81
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "lower_size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "upper_size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 16
                    }
                },
                "optional": True
            }
        ]
    }
}

