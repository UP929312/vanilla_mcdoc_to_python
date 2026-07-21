# Generated from symbols.json for ::java::data::worldgen::feature::GeodeLayerSettings
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class GeodeLayerSettings:
    filling: Annotated[float, 'Range | `0.01`-`50` | both inclusive'] | None = None
    inner_layer: Annotated[float, 'Range | `0.01`-`50` | both inclusive'] | None = None
    middle_layer: Annotated[float, 'Range | `0.01`-`50` | both inclusive'] | None = None
    outer_layer: Annotated[float, 'Range | `0.01`-`50` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::GeodeLayerSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "filling",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "inner_layer",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "middle_layer",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "outer_layer",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0.01,
                        "max": 50
                    }
                },
                "optional": True
            }
        ]
    }
}

