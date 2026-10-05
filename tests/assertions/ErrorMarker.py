# ~~~ WHAT ARE WE TESTING ~~~

# Showcases IntArray -> tuple[int, int, int]

# ~~~ FILE CONTENT ~~~
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
