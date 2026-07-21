# Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialConditionRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialCondition import MaterialCondition


type MaterialConditionRef = str | MaterialCondition


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::MaterialConditionRef": {
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
                                "value": "26.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "material_condition"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::material_condition::MaterialCondition"
            }
        ]
    }
}

