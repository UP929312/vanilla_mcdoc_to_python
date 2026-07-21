# Generated from symbols.json for ::java::data::worldgen::feature::OreConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.TargetBlock import TargetBlock


@dataclass(kw_only=True)
class OreConfig:
    targets: list[TargetBlock]
    size: Annotated[int, 'Range | `0`-`64` | both inclusive']
    discard_chance_on_air_exposure: Annotated[float, 'Range | `0`-`1` | both inclusive']  # Chance that feature placement will be discarded if the ore is exposed to air blocks.


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

