# Generated from symbols.json for ::java::data::loot::function::SetStewEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.loot.function.StewEffect import StewEffect


@dataclass(kw_only=True)
class SetStewEffect(Conditions):
    effects: list[StewEffect] | None = None  # Sets the status effects for suspicious stew.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetStewEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Sets the status effects for suspicious stew.",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::function::StewEffect"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

