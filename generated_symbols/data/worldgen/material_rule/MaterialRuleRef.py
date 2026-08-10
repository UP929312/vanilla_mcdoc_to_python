"""
Generated from symbols.json for ::java::data::worldgen::material_rule::MaterialRuleRef
Local link to file: generated_symbols/data/worldgen/material_rule/MaterialRuleRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_rule.MaterialRule import MaterialRule


type MaterialRuleRef = Annotated[str, IdSpec(registry='material_rule')] | MaterialRule


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

