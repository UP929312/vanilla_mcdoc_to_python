# Generated from symbols.json for ::java::data::loot::function::SetOminousBottleAmplifier
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class SetOminousBottleAmplifier(Conditions):
    amplifier: NumberProviderRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetOminousBottleAmplifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "amplifier",
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

