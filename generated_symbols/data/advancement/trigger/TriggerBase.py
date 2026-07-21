# Generated from symbols.json for ::java::data::advancement::trigger::TriggerBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class TriggerBase:
    player: CompositeEntity | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::TriggerBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "player",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::CompositeEntity"
                },
                "optional": True
            }
        ]
    }
}

