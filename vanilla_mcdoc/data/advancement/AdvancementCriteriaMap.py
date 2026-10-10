"""
Generated from symbols.json for ::java::data::advancement::AdvancementCriteriaMap
Local link to file: vanilla_mcdoc/data/advancement/AdvancementCriteriaMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterion


type AdvancementCriteriaMap = dict[str, AdvancementCriterion]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementCriteriaMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "criterion",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "definition": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "boolean",
                                            "value": True
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::AdvancementCriterion"
                }
            }
        ]
    }
}
