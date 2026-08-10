"""
Generated from symbols.json for ::java::data::worldgen::biome::CarversPerStep
Local link to file: generated_symbols/data/worldgen/biome/CarversPerStep.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.CarveStep import CarveStep
    from generated_symbols.data.worldgen.carver.CarverListRef import CarverListRef


type CarversPerStep = dict[CarveStep, CarverListRef]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::biome::CarversPerStep": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::CarveStep"
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::carver::CarverRef"
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18.2"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::carver::CarverListRef",
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
                            ]
                        }
                    ]
                }
            }
        ],
        "attributes": [
            {
                "name": "until",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.21.2"
                    }
                }
            }
        ]
    }
}

