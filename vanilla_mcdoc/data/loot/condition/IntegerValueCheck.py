"""
Generated from symbols.json for ::java::data::loot::condition::IntegerValueCheck
Local link to file: vanilla_mcdoc/data/loot/condition/IntegerValueCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.IntRange import IntRange
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class IntegerValueCheck(GeneratedModel):
    value: IntNumberProviderRef
    test: IntRange  # Passes when `value` is within the test range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::IntegerValueCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::IntNumberProviderRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Passes when `value` is within the test range.",
                "key": "test",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::IntRange"
                }
            }
        ]
    }
}
