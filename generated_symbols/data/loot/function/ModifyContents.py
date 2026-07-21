# Generated from symbols.json for ::java::data::loot::function::ModifyContents
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.item_modifier.ItemModifier import ItemModifier
    from generated_symbols.data.loot.function.ContainerComponents import ContainerComponents


@dataclass(kw_only=True)
class ModifyContents(Conditions):
    component: ContainerComponents  # Describes target component's items to modify.
    modifier: ItemModifier  # Applied to every item inside container.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ModifyContents": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Describes target component's items to modify.",
                "key": "component",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ContainerComponents",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Applied to every item inside container.",
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifier"
                }
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

