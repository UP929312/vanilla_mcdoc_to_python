"""
Generated from symbols.json for ::java::data::number_provider::legacy::EnvironmentAttributeNumberProvider
Local link to file: generated_symbols/data/number_provider/legacy/EnvironmentAttributeNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.NumericalEnvironmentAttribute import NumericalEnvironmentAttribute


class EnvironmentAttributeNumberProvider(GeneratedModel):
    attribute: NumericalEnvironmentAttribute


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::legacy::EnvironmentAttributeNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "attribute",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::NumericalEnvironmentAttribute"
                }
            }
        ]
    }
}
