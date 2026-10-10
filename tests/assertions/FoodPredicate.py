# ~~~ WHAT ARE WE TESTING ~~~

# A basic example, FoodPredicate
# References a type with type args, `MinMaxBounds[int]``, a Generic of type.
# Also shows that it has MinMaxBounds[type] | type, as the user should also be able to just do `int`
# Finally, it also shows the optional stuff, `| None = None`.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::advancement::predicate::FoodPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/FoodPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class FoodPredicate(GeneratedModel):
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None
