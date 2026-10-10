"""
Generated from symbols.json for ::java::data::worldgen::feature::OreConfig
Local link to file: generated_symbols/data/worldgen/feature/OreConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.TargetBlock import TargetBlock


class OreConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    targets: list[TargetBlock]
    size: Annotated[int, Field(ge=0, le=64)]
    discard_chance_on_air_exposure: Annotated[float, Field(ge=0, le=1)]  # Chance that feature placement will be discarded if the ore is exposed to air blocks.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::OreConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::TargetBlock"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "targets",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::TargetBlock"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 64
                    }
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "desc": "Chance that feature placement will be discarded if the ore is exposed to air blocks.",
                "key": "discard_chance_on_air_exposure",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

