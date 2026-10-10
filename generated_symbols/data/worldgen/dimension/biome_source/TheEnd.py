"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::TheEnd
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/TheEnd.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class TheEnd(GeneratedModel):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::TheEnd": {
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
                "key": "seed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                }
            }
        ]
    }
}
