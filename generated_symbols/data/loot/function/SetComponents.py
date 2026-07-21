# Generated from symbols.json for ::java::data::loot::function::SetComponents
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.world.component.DataComponentPatch import DataComponentPatch


@dataclass(kw_only=True)
class SetComponents(Conditions):
    components: DataComponentPatch


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetComponents": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPatch"
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

