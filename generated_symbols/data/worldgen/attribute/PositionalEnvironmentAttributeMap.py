# Generated from symbols.json for ::java::data::worldgen::attribute::PositionalEnvironmentAttributeMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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

