"""
Generated from symbols.json for ::java::data::advancement::trigger::PlacedBlockTrigger
Local link to file: generated_symbols/data/advancement/trigger/PlacedBlockTrigger.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.ItemUesdOnLocationConditions import ItemUesdOnLocationConditions


PlacedBlockTrigger = AllOptional[ItemUesdOnLocationConditions]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::PlacedBlockTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "union",
                "members": [
                    {
                        "kind": "reference",
                        "path": "::java::data::advancement::trigger::PlacedBlockConditions",
                        "attributes": [
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.20"
                                    }
                                }
                            }
                        ]
                    },
                    {
                        "kind": "reference",
                        "path": "::java::data::advancement::trigger::ItemUesdOnLocationConditions",
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.20"
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

