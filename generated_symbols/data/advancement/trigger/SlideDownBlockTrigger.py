"""
Generated from symbols.json for ::java::data::advancement::trigger::SlideDownBlockTrigger
Local link to file: generated_symbols/data/advancement/trigger/SlideDownBlockTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.BlockStateConditions import BlockStateConditions
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions


@dataclass(kw_only=True)
class SlideDownBlockTriggerTypeArg(BlockStateConditions, PlayerConditions):
    pass


SlideDownBlockTrigger = AllOptional[SlideDownBlockTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::SlideDownBlockTrigger": {
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

