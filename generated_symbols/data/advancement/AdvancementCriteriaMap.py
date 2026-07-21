# Generated from symbols.json for ::java::data::advancement::AdvancementCriteriaMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementCriterion import AdvancementCriterion


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

