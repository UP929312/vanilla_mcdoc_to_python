"""
Generated from symbols.json for ::java::data::advancement::trigger::ImpossibleTrigger
Local link to file: generated_symbols/data/advancement/trigger/ImpossibleTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional


@dataclass(kw_only=True)
class ImpossibleTriggerTypeArg:
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

