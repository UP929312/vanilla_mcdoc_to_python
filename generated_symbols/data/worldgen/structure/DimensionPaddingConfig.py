# Generated from symbols.json for ::java::data::worldgen::structure::DimensionPaddingConfig
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class DimensionPaddingConfig:
    bottom: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None
    top: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::DimensionPaddingConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "bottom",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "top",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

