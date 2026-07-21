# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::TheEnd
from dataclasses import dataclass


@dataclass(kw_only=True)
class TheEnd:
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

