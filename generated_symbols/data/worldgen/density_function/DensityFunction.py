# Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunction
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


@dataclass(kw_only=True)
class DensityFunctionStruct1:
    type: str

type DensityFunction = NoiseRange | DensityFunctionStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::DensityFunction": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::density_function::NoiseRange"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/density_function_type"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:density_function"
                        }
                    }
                ]
            }
        ]
    }
}

