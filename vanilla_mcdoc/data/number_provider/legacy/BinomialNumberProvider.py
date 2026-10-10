"""
Generated from symbols.json for ::java::data::number_provider::legacy::BinomialNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/legacy/BinomialNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.legacy.LegacyNumberProvider import LegacyNumberProvider


class BinomialNumberProvider(GeneratedModel):
    n: LegacyNumberProvider
    p: LegacyNumberProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::BinomialNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "n",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::legacy::LegacyNumberProvider"
                }
            },
            {
                "kind": "pair",
                "key": "p",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::legacy::LegacyNumberProvider"
                }
            }
        ]
    }
}
