# Generated from symbols.json for ::java::data::worldgen::density_function::InvervalSelect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


@dataclass(kw_only=True)
class InvervalSelect:
    input: DensityFunctionRef
    thresholds: Annotated[list[NoiseRange], 'Length = 1 (inclusive) and above']  # Must have exactly one fewer element than `functions`.
    functions: Annotated[list[DensityFunctionRef], 'Length = 2 (inclusive) and above']  # Must have exactly one more element than `thresholds`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::InvervalSelect": {
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
                "desc": "Must have exactly one fewer element than `functions`.",
                "key": "thresholds",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::density_function::NoiseRange"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Must have exactly one more element than `thresholds`.",
                "key": "functions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::density_function::DensityFunctionRef"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 2
                    }
                }
            }
        ]
    }
}

