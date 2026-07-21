# Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseGeneratorFlags
from dataclasses import dataclass


@dataclass(kw_only=True)
class NoiseGeneratorFlags:
    aquifers_enabled: bool
    ore_veins_enabled: bool


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseGeneratorFlags": {
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "noise_caves_enabled",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.18.2"
                            }
                        }
                    }
                ],
                "key": "noodle_caves_enabled",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "aquifers_enabled",
                "type": {
                    "kind": "boolean"
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
                                "value": "1.18"
                            }
                        }
                    }
                ],
                "key": "deepslate_enabled",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "ore_veins_enabled",
                "type": {
                    "kind": "boolean"
                }
            }
        ]
    }
}

