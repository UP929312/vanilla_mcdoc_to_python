"""
Generated from symbols.json for ::java::data::worldgen::structure::BuriedTreasure
Local link to file: generated_symbols/data/worldgen/structure/BuriedTreasure.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from generated_symbols.base import GeneratedModel


class BuriedTreasure(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::BuriedTreasure": {
        "kind": "struct",
        "fields": [
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
                "key": "probability",
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
