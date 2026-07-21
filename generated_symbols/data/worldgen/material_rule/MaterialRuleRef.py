# Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRuleRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_rule.MaterialRule import MaterialRule


type MaterialRuleRef = str | MaterialRule


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_rule::MaterialRuleRef": {
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
                                "value": "material_rule"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::material_rule::MaterialRule"
            }
        ]
    }
}

