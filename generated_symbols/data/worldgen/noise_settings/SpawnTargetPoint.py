# Generated from symbols.json for ::java::data::worldgen::noise_settings::SpawnTargetPoint
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.biome_source.ClimateParameter import ClimateParameter


type SpawnTargetPoint = dict[Annotated[str, IdSpec(registry='worldgen/density_function')], ClimateParameter]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::SpawnTargetPoint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
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
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::biome_source::ClimateParameter"
                }
            }
        ]
    }
}

