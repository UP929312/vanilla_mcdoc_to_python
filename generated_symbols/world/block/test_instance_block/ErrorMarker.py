"""
Generated from symbols.json for ::java::world::block::test_instance_block::ErrorMarker
Local link to file: generated_symbols/world/block/test_instance_block/ErrorMarker.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


class ErrorMarker(GeneratedModel):
    pos: tuple[int, int, int]
    text: Text


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::test_instance_block::ErrorMarker": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "pos",
                "type": {
                    "kind": "int_array",
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "text",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            }
        ]
    }
}

