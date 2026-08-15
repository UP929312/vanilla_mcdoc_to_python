"""
Generated from symbols.json for ::java::data::worldgen::attribute::PositionalEnvironmentAttributeMap
Local link to file: generated_symbols/data/worldgen/attribute/PositionalEnvironmentAttributeMap.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap
from generated_symbols.data.worldgen.attribute.PositionalEnvironmentAttribute import PositionalEnvironmentAttribute


PositionalEnvironmentAttributeMap = EnvironmentAttributeMap[PositionalEnvironmentAttribute]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::PositionalEnvironmentAttributeMap": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::worldgen::attribute::EnvironmentAttributeMap"
        },
        "typeArgs": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::attribute::PositionalEnvironmentAttribute"
            }
        ]
    }
}

