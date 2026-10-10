"""
Generated from symbols.json for ::java::data::loot::FloatRange
Local link to file: generated_symbols/data/loot/FloatRange.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class FloatRangeStruct(GeneratedModel):
    min: FloatNumberProviderRef | None = None
    max: FloatNumberProviderRef | None = None


type FloatRange = FloatNumberProviderRef | FloatRangeStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::FloatRange": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::number_provider::FloatNumberProviderRef"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "min",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::number_provider::FloatNumberProviderRef"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "max",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::number_provider::FloatNumberProviderRef"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}
