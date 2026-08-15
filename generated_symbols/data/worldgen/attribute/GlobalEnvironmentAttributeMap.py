"""
Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
Local link to file: generated_symbols/data/worldgen/attribute/GlobalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap
from generated_symbols.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId
from minecraft_registry import IdSpec


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::worldgen::attribute::EnvironmentAttributeMap"
        },
        "typeArgs": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "environment_attribute"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

