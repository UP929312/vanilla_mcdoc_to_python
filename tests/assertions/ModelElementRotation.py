# ~~~ WHAT ARE WE TESTING ~~~

# Collapses it's deprecated child - nice.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::model::ModelElementRotation
Local link to file: generated_symbols/assets/model/ModelElementRotation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.direction.Axis import Axis


type ModelElementRotation = dict[Axis, float]
