# Generated from symbols.json for ::java::data::worldgen::noise_settings::StructureSettings
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.ConcentricRingsPlacement import ConcentricRingsPlacement
    from generated_symbols.data.worldgen.structure_set.RandomSpreadPlacement import RandomSpreadPlacement


@dataclass(kw_only=True)
class StructureSettings:
    structures: dict[str, RandomSpreadPlacement]
    stronghold: ConcentricRingsPlacement | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::StructureSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "stronghold",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::ConcentricRingsPlacement"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "structures",
                "type": {
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
                                                "value": "worldgen/structure_feature"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::structure_set::RandomSpreadPlacement"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

