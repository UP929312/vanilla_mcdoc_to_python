# Generated from symbols.json for ::java::data::loot::function::SetRandomDyes
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class SetRandomDyes(Conditions):
    number_of_dyes: NumberProviderRef  # Applies specified number of random dyes to the item.  For example, one possible outcome of `"number_of_dyes": 2` is `#2C3065`, which is the combination of a blue dye and a black dye.  The same dye color can be selected multiple times.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetRandomDyes": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Applies specified number of random dyes to the item. \\\nFor example, one possible outcome of `\"number_of_dyes\": 2` is `#2C3065`, which is the combination of a blue dye and a black dye. \\\nThe same dye color can be selected multiple times.",
                "key": "number_of_dyes",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
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

