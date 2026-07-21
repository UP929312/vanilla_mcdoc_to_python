# Generated from symbols.json for ::java::data::worldgen::density_function::RangeChoice
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


@dataclass(kw_only=True)
class RangeChoice:
    input: DensityFunctionRef
    min_inclusive: NoiseRange
    max_exclusive: NoiseRange
    when_in_range: DensityFunctionRef
    when_out_of_range: DensityFunctionRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::RangeChoice": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "input",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "min_inclusive",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "max_exclusive",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::NoiseRange"
                }
            },
            {
                "kind": "pair",
                "key": "when_in_range",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            },
            {
                "kind": "pair",
                "key": "when_out_of_range",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                }
            }
        ]
    }
}

