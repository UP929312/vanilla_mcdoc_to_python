"""
Generated from symbols.json for ::java::data::util::ContextNbtProvider
Local link to file: generated_symbols/data/util/ContextNbtProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.NbtContextTarget import NbtContextTarget


class ContextNbtProvider(GeneratedModel):
    target: NbtContextTarget


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::ContextNbtProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::NbtContextTarget"
                }
            }
        ]
    }
}

