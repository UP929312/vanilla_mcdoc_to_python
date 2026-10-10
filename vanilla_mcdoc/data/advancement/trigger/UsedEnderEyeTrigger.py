"""
Generated from symbols.json for ::java::data::advancement::trigger::UsedEnderEyeTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/UsedEnderEyeTrigger.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class UsedEnderEyeTriggerTypeArg(PlayerConditions):
    distance: MinMaxBounds[float] | float | None = None  # Horizontal distance between the player and the stronghold.


UsedEnderEyeTrigger = AllOptional[UsedEnderEyeTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::UsedEnderEyeTrigger": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::advancement::trigger::AllOptional"
        },
        "typeArgs": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::PlayerConditions"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Horizontal distance between the player and the stronghold.",
                        "key": "distance",
                        "type": {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::util::MinMaxBounds"
                            },
                            "typeArgs": [
                                {
                                    "kind": "double"
                                }
                            ]
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}
