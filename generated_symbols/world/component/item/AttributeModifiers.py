# Generated from symbols.json for ::java::world::component::item::AttributeModifiers
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.AttributeModifier import AttributeModifier


@dataclass(kw_only=True)
class AttributeModifiers:
    modifiers: list[AttributeModifier]
    show_in_tooltip: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AttributeModifiers": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "modifiers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::component::item::AttributeModifier"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "show_in_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

