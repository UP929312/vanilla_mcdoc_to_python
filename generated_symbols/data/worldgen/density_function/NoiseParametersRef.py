# Generated from symbols.json for ::java::data::worldgen::density_function::NoiseParametersRef
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters


type NoiseParametersRef = Annotated[str, IdSpec(registry='worldgen/noise')] | NoiseParameters


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::NoiseParametersRef": {
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
                                "value": "worldgen/noise"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::dimension::biome_source::NoiseParameters"
            }
        ]
    }
}

