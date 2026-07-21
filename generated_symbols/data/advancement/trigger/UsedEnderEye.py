# Generated from symbols.json for ::java::data::advancement::trigger::UsedEnderEye
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class UsedEnderEye(TriggerBase):
    distance: MinMaxBounds[float] | float | None = None  # Horizontal distance between the player and the stronghold.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::UsedEnderEye": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
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
                            "kind": "float"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

