# Generated from symbols.json for ::java::data::worldgen::structure_set::RandomSpreadPlacement
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure_set.SpreadType import SpreadType


@dataclass(kw_only=True)
class RandomSpreadPlacement:
    spacing: Annotated[int, 'Range | `0`-`4096` | both inclusive']  # Average distance in chunks between two structures of this type.
    separation: Annotated[int, 'Range | `0`-`4096` | both inclusive']  # Minimum distance in chunks between two structures of this type.
    spread_type: SpreadType | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure_set::RandomSpreadPlacement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Average distance in chunks between two structures of this type.",
                "key": "spacing",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 4096
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Minimum distance in chunks between two structures of this type.",
                "key": "separation",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 4096
                    }
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "salt",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "spread_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure_set::SpreadType"
                },
                "optional": True
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
                                "value": "1.18.2"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "locate_offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 16
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

