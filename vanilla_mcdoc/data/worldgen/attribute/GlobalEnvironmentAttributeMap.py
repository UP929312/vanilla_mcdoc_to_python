"""
Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
Local link to file: vanilla_mcdoc/data/worldgen/attribute/GlobalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap
from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId


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
