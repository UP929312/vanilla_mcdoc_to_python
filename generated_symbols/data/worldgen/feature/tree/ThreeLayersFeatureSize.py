# Generated from symbols.json for ::java::data::worldgen::feature::tree::ThreeLayersFeatureSize
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ThreeLayersFeatureSize:
    min_clipped_height: Annotated[float, 'Range | `0`-`80` | both inclusive'] | None = None
    limit: Annotated[int, 'Range | `0`-`80` | both inclusive'] | None = None
    upper_limit: Annotated[int, 'Range | `0`-`80` | both inclusive'] | None = None
    lower_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None
    middle_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None
    upper_size: Annotated[int, 'Range | `0`-`16` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::ThreeLayersFeatureSize": {
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
                        "max": 80
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "upper_limit",
                "type": {
                    "kind": "int",
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
                "key": "middle_size",
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

