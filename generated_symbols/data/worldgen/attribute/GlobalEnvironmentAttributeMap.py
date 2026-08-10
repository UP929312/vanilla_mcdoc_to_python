"""
Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
Local link to file: generated_symbols/data/worldgen/attribute/GlobalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[Annotated[str, IdSpec(registry='environment_attribute')]]


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

