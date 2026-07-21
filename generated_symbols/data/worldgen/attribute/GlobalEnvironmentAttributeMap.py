# Generated from symbols.json for ::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap


GlobalEnvironmentAttributeMap = EnvironmentAttributeMap[str]


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

