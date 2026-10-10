"""
Generated from symbols.json for ::java::data::number_provider::legacy::UniformNumberProvider
Local link to file: generated_symbols/data/number_provider/legacy/UniformNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.legacy.LegacyNumberProvider import LegacyNumberProvider


class UniformNumberProvider(GeneratedModel):
    min: LegacyNumberProvider
    max: LegacyNumberProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::UniformNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::legacy::LegacyNumberProvider"
                }
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::legacy::LegacyNumberProvider"
                }
            }
        ]
    }
}
