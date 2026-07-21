# Generated from symbols.json for ::java::data::worldgen::noise_settings::NoiseGeneratorSettingsRef
from dataclasses import dataclass
from generated_symbols.data.worldgen.noise_settings.NoiseGeneratorSettings import NoiseGeneratorSettings


@dataclass(kw_only=True)
class NoiseGeneratorSettingsRefStruct1(NoiseGeneratorSettings):
    name: str

type NoiseGeneratorSettingsRef = str | NoiseGeneratorSettingsRefStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::noise_settings::NoiseGeneratorSettingsRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16.2"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/noise_settings"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "name",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "worldgen/noise_settings"
                                                }
                                            },
                                            "definition": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "boolean",
                                                    "value": True
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::noise_settings::NoiseGeneratorSettings"
                        }
                    }
                ]
            }
        ]
    }
}

