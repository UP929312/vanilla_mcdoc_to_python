"""
Generated from symbols.json for ::java::data::loot::condition::FloatValueCheck
Local link to file: vanilla_mcdoc/data/loot/condition/FloatValueCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.FloatRange import FloatRange
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class FloatValueCheck(GeneratedModel):
    value: FloatNumberProviderRef
    test: FloatRange  # Passes when `value` is within the test range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::FloatValueCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::FloatNumberProviderRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Passes when `value` is within the test range.",
                "key": "test",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::FloatRange"
                }
            }
        ]
    }
}
