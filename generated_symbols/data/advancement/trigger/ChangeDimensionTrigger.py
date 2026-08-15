"""
Generated from symbols.json for ::java::data::advancement::trigger::ChangeDimensionTrigger
Local link to file: generated_symbols/data/advancement/trigger/ChangeDimensionTrigger.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.advancement.trigger.AllOptional import AllOptional
from generated_symbols.data.advancement.trigger.PlayerConditions import PlayerConditions
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class ChangeDimensionTriggerTypeArg(PlayerConditions):
    from_: Annotated[str, IdSpec(registry='dimension')] | None = None
    to: Annotated[str, IdSpec(registry='dimension')] | None = None


ChangeDimensionTrigger = AllOptional[ChangeDimensionTriggerTypeArg]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ChangeDimensionTrigger": {
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
                        "key": "from",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "dimension"
                                        }
                                    }
                                }
                            ]
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "to",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "dimension"
                                        }
                                    }
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

