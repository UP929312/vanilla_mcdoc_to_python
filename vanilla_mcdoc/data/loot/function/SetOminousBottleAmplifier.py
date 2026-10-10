"""
Generated from symbols.json for ::java::data::loot::function::SetOminousBottleAmplifier
Local link to file: vanilla_mcdoc/data/loot/function/SetOminousBottleAmplifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class SetOminousBottleAmplifier(Conditions):
    amplifier: IntNumberProviderRef


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
                    "path": "::java::data::number_provider::IntNumberProviderRef"
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
