# Generated from symbols.json for ::java::data::loot::function::SetCustomData
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.world.component.CustomData import CustomData


@dataclass(kw_only=True)
class SetCustomData(Conditions):
    tag: CustomData


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetCustomData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "tag",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::CustomData"
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

