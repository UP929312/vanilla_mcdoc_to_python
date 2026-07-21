# Generated from symbols.json for ::java::data::worldgen::feature::ModernPatchConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.FeatureRef import FeatureRef


@dataclass(kw_only=True)
class ModernPatchConfig:
    feature: FeatureRef
    xz_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 7.
    y_spread: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to 3.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ModernPatchConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 7.",
                "key": "xz_spread",
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
                "desc": "Defaults to 3.",
                "key": "y_spread",
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
                "key": "feature",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::FeatureRef"
                }
            }
        ]
    }
}

