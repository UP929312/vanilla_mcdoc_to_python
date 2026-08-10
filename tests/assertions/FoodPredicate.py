# ~~~ WHAT ARE WE TESTING ~~~

# A basic example, FoodPredicate
# References a type with type args, `MinMaxBounds[int]``, a Generic of type.
# Also shows that it has MinMaxBounds[type] | type, as the user should also be able to just do `int`
# Finally, it also shows the optional stuff, `| None = None`.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::advancement::predicate::FoodPredicate
Local link to file: generated_symbols/data/advancement/predicate/FoodPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class FoodPredicate:
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None
