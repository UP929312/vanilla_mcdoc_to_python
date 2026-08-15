"""
Generated from symbols.json for ::java::data::advancement::trigger::ItemUsedOnLocationTrigger
Local link to file: generated_symbols/data/advancement/trigger/ItemUsedOnLocationTrigger.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.ItemUesdOnLocationConditions import ItemUesdOnLocationConditions


ItemUsedOnLocationTrigger = AllOptional[ItemUesdOnLocationConditions]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ItemUsedOnLocationTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "reference",
                "path": "::java::data::advancement::trigger::ItemUesdOnLocationConditions"
            }
        ]
    }
}

