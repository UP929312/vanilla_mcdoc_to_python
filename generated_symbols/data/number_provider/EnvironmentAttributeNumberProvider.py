"""
Generated from symbols.json for ::java::data::number_provider::EnvironmentAttributeNumberProvider
Local link to file: generated_symbols/data/number_provider/EnvironmentAttributeNumberProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.NumericalEnvironmentAttribute import NumericalEnvironmentAttribute


@dataclass(kw_only=True)
class EnvironmentAttributeNumberProvider:
    attribute: NumericalEnvironmentAttribute


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::EnvironmentAttributeNumberProvider": {
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

