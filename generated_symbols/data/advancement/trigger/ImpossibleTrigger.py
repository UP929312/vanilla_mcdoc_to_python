"""
Generated from symbols.json for ::java::data::advancement::trigger::ImpossibleTrigger
Local link to file: generated_symbols/data/advancement/trigger/ImpossibleTrigger.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel
from generated_symbols.data.advancement.trigger.AllOptional import AllOptional


class ImpossibleTriggerTypeArg(GeneratedModel):
    pass


ImpossibleTrigger = AllOptional[ImpossibleTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ImpossibleTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "struct",
                "fields": []
            }
        ]
    }
}

