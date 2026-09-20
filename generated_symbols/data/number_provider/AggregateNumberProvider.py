"""
Generated from symbols.json for ::java::data::number_provider::AggregateNumberProvider
Local link to file: generated_symbols/data/number_provider/AggregateNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.AggregateOperands import AggregateOperands


class AggregateNumberProvider(GeneratedModel):
    operands: AggregateOperands


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::AggregateNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "summands",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderListRef"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "operands",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::AggregateOperands"
                }
            }
        ]
    }
}

