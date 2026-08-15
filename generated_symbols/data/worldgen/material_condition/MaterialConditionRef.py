"""
Generated from symbols.json for ::java::data::worldgen::material_condition::MaterialConditionRef
Local link to file: generated_symbols/data/worldgen/material_condition/MaterialConditionRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.material_condition.MaterialCondition import MaterialCondition
    from generated_symbols.registry.KnownMaterialConditionId import KnownMaterialConditionId


type MaterialConditionRef = Annotated[str, IdSpec(registry='material_condition')] | KnownMaterialConditionId | MaterialCondition


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

