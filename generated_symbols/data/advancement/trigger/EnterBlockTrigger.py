"""
Generated from symbols.json for ::java::data::advancement::trigger::EnterBlockTrigger
Local link to file: generated_symbols/data/advancement/trigger/EnterBlockTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class EnterBlockTriggerTypeArg(BlockStateConditions, PlayerConditions):
    pass


EnterBlockTrigger = AllOptional[EnterBlockTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::EnterBlockTrigger": {
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
                        "kind": "spread",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::advancement::trigger::BlockStateConditions"
                        }
                    }
                ]
            }
        ]
    }
}

