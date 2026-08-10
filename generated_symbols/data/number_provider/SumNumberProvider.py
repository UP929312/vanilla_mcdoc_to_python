"""
Generated from symbols.json for ::java::data::number_provider::SumNumberProvider
Local link to file: generated_symbols/data/number_provider/SumNumberProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderListRef import NumberProviderListRef


@dataclass(kw_only=True)
class SumNumberProvider:
    summands: NumberProviderListRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::SumNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "summands",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderListRef"
                }
            }
        ]
    }
}

