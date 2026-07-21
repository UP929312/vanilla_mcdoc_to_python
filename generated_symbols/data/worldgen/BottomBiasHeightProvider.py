# Generated from symbols.json for ::java::data::worldgen::BottomBiasHeightProvider
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider


@dataclass(kw_only=True)
class BottomBiasHeightProvider(UniformHeightProvider):
    inner: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::BottomBiasHeightProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::UniformHeightProvider"
                }
            },
            {
                "kind": "pair",
                "key": "inner",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

