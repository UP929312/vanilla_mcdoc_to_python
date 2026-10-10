"""
Generated from symbols.json for ::java::data::advancement::trigger::StartRidingTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/StartRidingTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


StartRidingTrigger = AllOptional[PlayerConditions]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::StartRidingTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "reference",
                "path": "::java::data::advancement::trigger::PlayerConditions"
            }
        ]
    }
}
