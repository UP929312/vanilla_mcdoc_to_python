"""
Generated from symbols.json for ::java::data::worldgen::attribute::PositionalEnvironmentAttribute
Local link to file: generated_symbols/data/worldgen/attribute/PositionalEnvironmentAttribute.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type PositionalEnvironmentAttribute = Annotated[str, IdSpec(registry='environment_attribute', exclude=('gameplay/fast_lava', 'gameplay/sky_light_level'))]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::PositionalEnvironmentAttribute": {
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
                                "value": "environment_attribute"
                            }
                        },
                        "exclude": {
                            "kind": "tree",
                            "values": {
                                "0": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "gameplay/fast_lava"
                                    }
                                },
                                "1": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "gameplay/sky_light_level"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ]
    }
}

