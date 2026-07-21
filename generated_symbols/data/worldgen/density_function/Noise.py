# Generated from symbols.json for ::java::data::worldgen::density_function::Noise
from dataclasses import dataclass


@dataclass(kw_only=True)
class Noise:
    noise: str
    xz_scale: float
    y_scale: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::Noise": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "noise",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/noise"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "xz_scale",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "y_scale",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

