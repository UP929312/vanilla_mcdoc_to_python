"""
Generated from symbols.json for ::java::assets::block_state_definition::MultiPartAlternatives
Local link to file: generated_symbols/assets/block_state_definition/MultiPartAlternatives.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


class MultiPartAlternatives(GeneratedModel):
    OR: list[MultiPartCondition]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::MultiPartAlternatives": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "OR",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::block_state_definition::MultiPartCondition"
                    }
                }
            }
        ]
    }
}
