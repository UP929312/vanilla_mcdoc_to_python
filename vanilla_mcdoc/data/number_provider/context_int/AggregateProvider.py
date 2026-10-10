"""
Generated from symbols.json for ::java::data::number_provider::context_int::AggregateProvider
Local link to file: vanilla_mcdoc/data/number_provider/context_int/AggregateProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.AggregateOperands import AggregateOperands


class AggregateProvider(GeneratedModel):
    inputs: AggregateOperands


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_int::AggregateProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "inputs",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::context_int::AggregateOperands"
                }
            }
        ]
    }
}
