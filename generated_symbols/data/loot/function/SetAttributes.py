# Generated from symbols.json for ::java::data::loot::function::SetAttributes
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.loot.function.AttributeModifier import AttributeModifier


@dataclass(kw_only=True)
class SetAttributes(Conditions):
    modifiers: list[AttributeModifier]  # List of attribute modifiers to apply to this item.
    replace: bool | None = None  # Whether to replace existing attributes (otherwise append to existing). Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetAttributes": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of attribute modifiers to apply to this item.",
                "key": "modifiers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::function::AttributeModifier"
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Whether to replace existing attributes (otherwise append to existing). Defaults to `True`.",
                "key": "replace",
                "type": {
                    "kind": "boolean"
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

