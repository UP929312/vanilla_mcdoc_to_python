# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::MultiNoiseBase
from dataclasses import dataclass


@dataclass(kw_only=True)
class MultiNoiseBase:
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::MultiNoiseBase": {
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
                                "value": "1.18"
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

