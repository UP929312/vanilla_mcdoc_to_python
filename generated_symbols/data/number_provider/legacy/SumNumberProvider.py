"""
Generated from symbols.json for ::java::data::number_provider::legacy::SumNumberProvider
Local link to file: generated_symbols/data/number_provider/legacy/SumNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.legacy.LegacyNumberProvider import LegacyNumberProvider


class SumNumberProvider(GeneratedModel):
    summands: list[LegacyNumberProvider]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::SumNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "summands",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::number_provider::legacy::LegacyNumberProvider"
                    }
                }
            }
        ]
    }
}

