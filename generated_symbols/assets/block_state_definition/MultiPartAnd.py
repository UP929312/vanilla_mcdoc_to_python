"""
Generated from symbols.json for ::java::assets::block_state_definition::MultiPartAnd
Local link to file: generated_symbols/assets/block_state_definition/MultiPartAnd.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


class MultiPartAnd(GeneratedModel):
    AND: list[MultiPartCondition]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::MultiPartAnd": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "AND",
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

