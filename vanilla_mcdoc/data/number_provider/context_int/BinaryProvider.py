"""
Generated from symbols.json for ::java::data::number_provider::context_int::BinaryProvider
Local link to file: generated_symbols/data/number_provider/context_int/BinaryProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.context_int.IntRef import IntRef


class BinaryProvider(GeneratedModel):
    left: IntRef
    right: IntRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_int::BinaryProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "left",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::context_int::IntRef"
                }
            },
            {
                "kind": "pair",
                "key": "right",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::context_int::IntRef"
                }
            }
        ]
    }
}
