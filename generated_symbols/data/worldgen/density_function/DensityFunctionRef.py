# Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunctionRef
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.DensityFunction import DensityFunction


type DensityFunctionRef = Annotated[str, IdSpec(registry='worldgen/density_function')] | DensityFunction


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::DensityFunctionRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/density_function"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::density_function::DensityFunction"
            }
        ]
    }
}

