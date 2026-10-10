# ~~~ WHAT ARE WE TESTING ~~~

# Collapses it's deprecated child - nice.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::model::ModelElementRotation
Local link to file: vanilla_mcdoc/assets/model/ModelElementRotation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Axis import Axis


type ModelElementRotation = dict[Axis, float]
