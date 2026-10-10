"""
Generated from symbols.json for ::java::data::advancement::trigger::ChangeDimensionTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/ChangeDimensionTrigger.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.minecraft_types import IdSpec


class ChangeDimensionTriggerTypeArg(PlayerConditions):
    from_: Annotated[str, IdSpec(registry='dimension')] | None = Field(default=None, alias='from')
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
